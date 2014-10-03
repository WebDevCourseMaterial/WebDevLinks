#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import jinja2
import webapp2

jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  autoescape=True)

USERNAME = "fisherds"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/links.html")
        # Tuple format is ("Display Name", is_this_a_folder_of_exercises, link or static folder path, number of exercises in folder)
        appengine_units = []
        appengine_units.append(("MovieQuotes", False, "http://" + USERNAME + "-movie-quotes.appspot.com"))
        appengine_units.append(("Weatherpics", False, "http://" + USERNAME + "-weatherpics.appspot.com"))
        appengine_units.append(("Guestbook", False, "http://" + USERNAME + "-guestbook.appspot.com"))
        appengine_units.append(("GradeRecorder", False, "http://" + USERNAME + "-grade-recorder.appspot.com"))
        appengine_units.append(("Dice with Friends", False, "http://" + USERNAME + "-dice-with-friends.appspot.com"))
        css_units = []
        css_units.append(("HTML Basics - Tag Practice", True, "/static/HtmlBasics/tagPractice", 10))
        js_units = []
        endpoints_angular_ajax_units = []
        tracks = []
        # Tuple format is ("Track name", units array)
        tracks.append(("AppEngine Track", appengine_units))
        tracks.append(("CSS Track", css_units))
        tracks.append(("JavaScript Track", js_units))
        tracks.append(("Endpoints Track", endpoints_angular_ajax_units))
        self.response.out.write(template.render({"username": USERNAME, "tracks": tracks}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
