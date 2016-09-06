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
        appengine_track.append(("Exam 1 - (Exam title)", False, "http://" + USERNAME + "-(exam-title).appspot.com"))
        appengine_track.append(("Guestbook", False, "http://" + USERNAME + "-guestbook.appspot.com"))
        appengine_track.append(("GradeRecorder", False, "http://" + USERNAME + "-grade-recorder.appspot.com"))
        appengine_track.append(("Dice with Friends", False, "http://" + USERNAME + "-dice-with-friends.appspot.com"))

        css_track = []
        css_track.append(("HTML Basics - Tag Practice", True, "/static/HtmlBasics/tagPractice", 10))  # These links won't work yet.  That's ok.

        js_track = []

        endpoints_ajax_track = []

        project = []
        project.append(("Product Idea Sheets", False, "http://add_google_doc_url"))
        project.append(("Mocks", False, "http://add_mock_url"))
        project.append(("Project Planning doc", False, "http://add_google_doc_url"))
        project.append(("Source code", False, "http://add_github_or_ada_url"))
        project.append(("Sprint Planning doc", False, "http://add_google_doc_url"))
        project.append(("Technical documentation", False, "http://add_github_or_ada_url"))
        project.append(("YouTube Video", False, "http://add_youtube_url"))
        project.append(("Final Product", False, "http://add_yourproject_link"))

        tracks = []
        # Tuple format is ("Track name", List of links)
        tracks.append(("AppEngine Track", appengine_track))
        tracks.append(("CSS Track", css_track))
        tracks.append(("JavaScript Track", js_track))
        tracks.append(("Endpoints Track", endpoints_ajax_track))
        tracks.append(("Project", project))
        self.response.out.write(template.render({"username": USERNAME, "tracks": tracks}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
