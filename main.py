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
form = '''
<form action="/testform">
	<input name="q">
	<input type="submit">
</form>
'''


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
        #q = self.request.get('q')
        #self.response.write(q)

        self.response.headers['Content-type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
