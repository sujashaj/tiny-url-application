from flask import Blueprint, request, redirect, abort
from dao.MongoDao import MongoDao
from dao.RedisDao import RedisDao
from tiny_url_management.TinyUrlManager import TinyUrlManager


class Routes:
    def __init__(self):
        self.bp = Blueprint("routes", __name__)
        self.host = "http://localhost:8080/"
        self.register_routes()
        self.tiny_url_manager = TinyUrlManager(RedisDao(), MongoDao())

    def home(self):
        return "Welcome to the Tiny Url Management Application!"

    def redirect_to_full_url(self, short_url):
        full_url = self.tiny_url_manager.get_url(short_url)
        if full_url:
            return redirect(full_url, code=302)
        else:
            abort(404)

    def generate_tiny_url(self, full_url):
        key = self.tiny_url_manager.generate_key(full_url)
        return {'tiny_url': self.host + key}, 200

    def register_routes(self):
        self.bp.add_url_rule("/", "home", self.home)
        self.bp.add_url_rule("/<short_url>", "redirect_to_full_url", self.redirect_to_full_url, methods=["GET"])
        self.bp.add_url_rule("/generate_tiny_url", "generate_tiny_url", self.redirect_to_full_url, methods=["POST"])