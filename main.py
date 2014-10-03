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

USERNAME = "yourusername"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("templates/links.html")
        # Tuple format is ("Display Name", is_this_a_static_folder_of_exercises, link or static folder path, number of exercises in folder)

        appengine_track = []
        appengine_track.append(("MovieQuotes", False, "http://" + USERNAME + "-movie-quotes.appspot.com"))
        appengine_track.append(("Weatherpics", False, "http://" + USERNAME + "-weatherpics.appspot.com"))
        appengine_track.append(("Guestbook", False, "http://" + USERNAME + "-guestbook.appspot.com"))
        appengine_track.append(("GradeRecorder", False, "http://" + USERNAME + "-grade-recorder.appspot.com"))
        appengine_track.append(("Dice with Friends", False, "http://" + USERNAME + "-dice-with-friends.appspot.com"))

        css_track = []
        css_track.append(("HTML Basics - Tag Practice", True, "/static/HtmlBasics/tagPractice", 10))

        js_track = []

        endpoints_angular_ajax_track = []

        project = []
        project.append(("Product Idea Sheet", False, "http://add_google_doc_url"))
        project.append(("Ninja Mock", False, "http://add_ninja_mock_url"))
        project.append(("Final Product", False, "http://add_yourproject_link"))

        tracks = []
        # Tuple format is ("Track name", List of links)
        tracks.append(("AppEngine Track", appengine_track))
        tracks.append(("CSS Track", css_track))
        tracks.append(("JavaScript Track", js_track))
        tracks.append(("Endpoints Track", endpoints_angular_ajax_track))
        tracks.append(("Project", project))
        self.response.out.write(template.render({"username": USERNAME, "tracks": tracks}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
