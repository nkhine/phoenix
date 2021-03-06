#The Phoenix project roadmap

More info at [https://trello.com/zmgc](https://trello.com/zmgc)

The following list is just for this prototype, but the ideas can be applied using any other framework, provided the libraries are supported by the language/application used to develop.

1. wireframes for main portal and chapter sites
2. questionnaire module - MCQ, MAQ and Free text input, so that it can be also used as a Poll
3. user profile, allow sites to control what data they want to store
4. video room - integrate nodejs using the python library to create a chat/video room see http://driv.in
5. enhance the existing style, perhaps use YUI2 grids, this way we can have a template that can be control by each individual users' preferences
6. right-to-left template for: 
 Arabic alphabet - used for Arabic, Persian, Urdu and many other languages.
 Hebrew alphabet - used for Hebrew, Yiddish and some other Jewish languages.
 Syriac alphabet - used for varieties of the Syriac language.
 Thaana - used for Dhivehi.
 N'Ko script - used for several languages of Africa.
8. up-to-down template for Mandarin Cantonese Taiwanese Shanghainese Japanese languages
9. mobile
10. create import scripts for different forums, wikis and documents from drupal, joomla, phpboard, wordpress etc... link these to the appropriate module, so if we are on the Forum, the user should have a tab 'Import'
11. ikaaro.turk - this will be a separate module, similar to ikaaro.wiki, and is based on mTurk from Amazon Web Services, where 'work' is distributed across many persons, thus the result is achieved much faster. For example, if we have an Open Office document, written in English, then the ikaaro.turk module will: 
	a. create a 'clone' of the document in how ever many languages that the original document needs to be translated in
	b. each 'clone', will then be split into small sections, if the document is 1,000 words containing 25 paragraphs then it will be split in 5 paragraphs (~ 200 words per paragraph)
	c. we will then have a form, which will contain:
	
	~~~
	-----------------------
	original 200 word text
	-----------------------

	[button ... (Translate)] - when clicked, an input form is created
 
	[input form for the translator to type into]

	[button ... (Submit)]
	~~~

	Using this model, we can distribute the translation work to many members. And as we are using Git we can then automatically merge all the sections, back to the main translated document.

	We must build workflows that is related to the size of the document and split the content by the amount of volunteers who have accepted to work on this, so if 25 people volunteer to help to translate the document, then the 25 paragraphs will be one paragraph by a person.

	Extendability - the same workflow can apply to other media projects, for example if we need a sound file to be transcoded, we can calculate the length of the sound file (for this example, lets say it is 10 minutes), and the language is English.

	We have a button (Call for Action...) on a form that contains the file, when a volunteer clicks on this button, we register that this person wants to help in transcoding the sound file. At the end of a set period, hopefully we can have 10 people willing to transcode the sound file. The sound file is then pushed through Audacity and split into 10 chunks of 1 minute each.

	A form is then presented with the 1 minute file and an input form for the transcoder to type the text. When all 10 chunks have been transcoded the text can then be pushed into the translation workflow, as discussed in the first example. So we have also a translation of the transcoded file.

	Then this transcoded and translated piece of work can be sent to the voice over group for the specific language where a new recording can be made in that language. Or the subtitle group etc...

	core tools to use: audacity, python's NLMP library which will be used to process the raw text data. maybe even push this into an mechanical translation service, so that most of the work is done and then a human volunteer can simply verify that the text makes sense.
 
12. set workflow for images, where the raw file (.psd, .gimp etc...) is uploaded, and other artists can localize this. 

13. Search - create the autofill so that [http://localhost:8080/;search?text=''&output=json](http://localhost:8080/;search?text=''&output=json) so in my class if the output is json this can then be pushed into the autofill, otherwise on submit, we just return the results on the page.

14. for mass server processing create an army of clustered hardware and launch this using boto and ec2, each chapter co-ordinator should setup a AWS account and setup a user, who can use the resources. Then if we have 10 chapters with AWS accounts, we can launch 200 micro-instances to distribute the work load. so the overall cost will be much lower, then having one big instance or using the existing server to do the heavy work.

15. Video and Audio streaming - custom jPlayer widget, to link files uploaded or linked in the user's profile page/playlist use, see the http://code.google.com/apis/youtube/2.0/reference.html#youtube_data_api_tag_media:content

	here is the example for TZMOfficialChannel [http://gdata.youtube.com/feeds/api/users/TZMOfficialChannel/uploads?v=2&alt=jsonc](http://gdata.youtube.com/feeds/api/users/TZMOfficialChannel/uploads?v=2&alt=jsonc) 

	also see this: [http://code.google.com/apis/youtube/articles/view_youtube_jsonc_responses.html](http://code.google.com/apis/youtube/articles/view_youtube_jsonc_responses.html)

	also look at the [http://icant.co.uk/easy-youtube/](http://icant.co.uk/easy-youtube/) perhaps it can be integrated.

	Using jPlayer it is not possible (well i have not found a way yet) to stream the YouTube video, I will have to hack the zPlayer module and create a template so that if the user adds a link to a video such as YouTube/Vimeo this is correctly displayed in the zPlayer.

	Also create a new class so that we can pull the metadata values directly from the YouTube API, here is an example code:

	~~~
	import gdata.youtube
	import gdata.youtube.service
	yt_service = gdata.youtube.service.YouTubeService()
	yt_service.ssl = True
	yt_service.developer_key = '53cr3t'
	yt_service.client_id = 'zeitgeist'
	~~~

	and see [http://code.google.com/apis/youtube/1.0/developers_guide_python.html#RetrievingVideoEntry](http://code.google.com/apis/youtube/1.0/developers_guide_python.html#RetrievingVideoEntry)

16. pipes.yahoo.com - to aggregate the content from different sites not on the Phoenix.

	example: [http://pipes.yahoo.com/pipes/pipe.run?_id=26ca074a13d28a8ad64e154a76244d43&_callback=eYTp.getFeed&_render=json&s=TZMOfficialChannel](http://pipes.yahoo.com/pipes/pipe.run?_id=26ca074a13d28a8ad64e154a76244d43&_callback=eYTp.getFeed&_render=json&s=TZMOfficialChannel)

17. User profile - make user's skills a prominent requirement so that you can then link these skills to the projects. for example a user adds a project, from the project description it will be possible to pull out a number of tags and then match this with a persons who's skills may fulfill the requirements for the project.
an example script based on project data pulled from [http://www.tzmnetwork.com/forums/topic/61/education-amp-art](http://www.tzmnetwork.com/forums/topic/61/education-amp-art):

	~~~
	>>>  from nltk import pos_tag, word_tokenize
	>>>  description = """Hello. \
	I'm Irish but based in France. At the moment, I'm working to create a business/charity which incorporates a traditional montessori school and artists ateliers in the same building. Practical education should be an important part of the process for the Zeitgeist movement and the principles which I am working towards are very compatible with the Zeitgeist movements declared aspirations. \
	There is a lot of discussion here but education is more than that. It hardwires the young person to think for themselves as opposed to adding untraditional thought patterns, in later years. It also creates a dynamic peer group. \
	This school is for children aged 3-18 years. The artists will be adults. I'm hoping to be able to facilitate education for both groups using the principles of montessori education. Whether the adults can learn as much as the children is a question. The expectation and plan is that they can cross pollinate. The children's school (3-18 years) will involve education in the arts and science. Covering traditional topics, creative practices and environmental awareness and systems of living.\
	I'm looking for financial aid or guidance, to raise the finances required. This will be the second school in france, though radically different to the first. \
	My intention is to look to foundations in the USA, UK, Ireland and France. Asking foundations for aid is not something which I have any experience with, so if there is anyone here who has, I would appreciate any constructive advice you can offer.\
	The school / arts atelier and training centre, has a volume of 3000 metres square or 9000 square feet. It's in a slightly run down factory on the edge of Paris, in a poor area within ile de France and will need total refurbishment. \
	The first school was much smaller than this, being of 110 metres square and is a great success. This second one is obviously a much larger project. \
	I can send references to anyone interested in becoming involved. Feel free to email me. \
	best regards \
	Tom""""
	>>> tagged_description = pos_tag(word_tokenize(description))
	>>> default_tagger.tag(tagged_description)
	[(('Hello.', 'NN'), 'NN'), (('I', 'PRP'), 'NN'), (("'m", 'VBP'), 'NN'), (('Irish', 'JJ'), 'NN'), (('but', 'CC'), 'NN'), (('based', 'VBN'), 'NN'), (('in', 'IN'), 'NN'), (('France.', 'NNP'), 'NN'), (('At', 'NNP'), 'NN'), (('the', 'DT'), 'NN'), (('moment', 'NN'), 'NN'), ((',', ','), 'NN'), (('I', 'PRP'), 'NN'), (("'m", 'VBP'), 'NN'), (('working', 'VBG'), 'NN'), (('to', 'TO'), 'NN'), (('create', 'VB'), 'NN'), (('a', 'DT'), 'NN'), (('business/charity', 'NN'), 'NN'), (('which', 'WDT'), 'NN'), (('incorporates', 'VBZ'), 'NN'), (('a', 'DT'), 'NN'), (('traditional', 'JJ'), 'NN'), (('montessori', 'NN'), 'NN'), (('school', 'NN'), 'NN'), (('and', 'CC'), 'NN'), (('artists', 'NNS'), 'NN'), (('ateliers', 'NNS'),

	>>> nltk.help.upenn_tagset('RB')
	RB: adverb
	occasionally unabatingly maddeningly adventurously professedly
	stirringly prominently technologically magisterially predominately
	swiftly fiscally pitilessly ...
	>>> nltk.help.upenn_tagset('NN')
	NN: noun, common, singular or mass
	common-carrier cabbage knuckle-duster Casino afghan shed thermostat
	investment slide humour falloff slick wind hyena override subhumanity
	machinist ...
	>>> nltk.help.upenn_tagset('VB')
	VB: verb, base form
	ask assemble assess assign assume atone attention avoid bake balkanize
	bank begin behold believe bend benefit bevel beware bless boil bomb
	boost brace break bring broil brush build ...
	~~~
        
	Now that we have the 'description' broken down by verbs, nouns etc... we can match against user profile data and suggest to the user possible members who may be able to help with the project.

	Obviously we can go deeper using the NLTK library and analyze the project description more accurately, but this is a further study, for more information see, Chapter 7: [http://nltk.googlecode.com/svn/trunk/doc/book/ch07.html](http://nltk.googlecode.com/svn/trunk/doc/book/ch07.html)

#Video
ZSight is an application level, highly programmable, interactive video service framework for building social interaction and collaboration around video content that acknowledges the increasing popularity of video as an integral part of communication and social networking applications. It provides a rich end-user experience in an environment powered by metadata communicated alongside the video, where the video content and expression thereof can be highly integrated. 
These notions include 'surfacing' of ideas and information 'buried' in the video somewhere within the content and directly expose these through the concept of timeline based tagging, blogging, chat and commentary that relate to segments of the video. Such dynamic tagging and commentary can drive the visual experience to the next level, bringing up time dependent contextually related information and allowing users to rapidly find video material meeting their needs. 
Shared comments can be captured on meetings, presentations and lectures that are recorded and further discussed, searched and edited to drive the overall value of the video content higher. The programmability of the framework will allow new value propositions to be created through different ratings, alternative context filtering etc., where the video is central and key to a whole new experience. The framework will build upon existing Open Source video platforms. See [https://trello.com/card/html5-chat-webapp/4f26b33d0e3dc6af1ce1c851/20](https://trello.com/card/html5-chat-webapp/4f26b33d0e3dc6af1ce1c851/20)


Another goal is to surface information buried in previous meeting recordings by making it accessible from a collaborative point of view, as well as from an information mining aspect. It will enable users to upload recorded meeting video and/or audio, automatically create transcriptions and attach metadata such as micro tags and comments. Tags and comments are identified along the meeting timeline highlighting items and segments of interest. The metadata can be edited and improved upon through collaboration. Metadata is used to facilitate searching for segments of interest, as well as collaboration and discussion.

#Storage

Create storage for the messages, so that when the page is refreshed or when the user has logged in, there is a list of all the messages that have been sent.

	user_id, users, message

	user_id - this is the user who sent the message
	users - tuple of all the users who got the message, this will allow us to filter by recipients
	message - lang;the actual message

	alternative solution is to put the data into postgre db, something:

	    everyone.now.sendGb = function(message) {
	        client.query(
	            'INSERT INTO messages SET owner_id = ?, user_id = ?, message = ?',
	            [message.id, message.user_id, sanitize(message.message).entityEncode().trim()],
	            function(err, info) {
	                if (!err) {
	                    everyone.now.pushMessage(message.message);
	                }
	            }
	        );
	    };


into a riak cluster see http://riakjs.org/:

    // npm install riak-js@latest
    var db = require('riak-js').getClient({host: "riak.myhost", port: "8098" });
    db.save('user', {users: ['user_id', 'user_id_n'...]}, 'message', 'timestamp'});

current [chat.zmgc.net](chat.zmgc.net) uses MangoDB see [https://github.com/nkhine/chat](https://github.com/nkhine/chat) for the code - this will be merged into the Phoenix project as a widget.
    
Also we need to utilise the local storage, html5.

#Google Fusion Table

Utilise Google Fusion Table to pull data into the application, here is an example on how to connect to a Google Fusion Table that lists the URL's for both the International and Regional chapters.

We can then link this into the Z-Tabzilla widget [https://github.com/TZM/Z-Tabzilla](https://github.com/TZM/Z-Tabzilla) and also within the [http://zmgc.net/;maps](http://zmgc.net/;maps) page where we can have a filter to display National and/or Regional Chapters.

An idea would also be to have more then one overlay, so for example, the user can switch to a Google Map rather then the existing D3.js map, although in the spirit of the project we ought to break away from depending on commercially oriented service providers.

It is hoped that we can provide Data Connectors to most file types and feed this data into a visual engine such as D3.js, so that if data in one part of the network changes this is reflected on all parts of the network.
 
	>>> import csv
	>>> import urllib2, urllib

	>>> request_url = 'https://www.google.com/fusiontables/api/query' 

	>>> query = 'SELECT * FROM 3027809 LIMIT 10' # 3027809 is the table Id, which you can get from File -> About this table
	>>> url = "%s?%s" % (request_url, urllib.urlencode({'sql': query}))
	>>> serv_req = urllib2.Request(url=url)
	>>> serv_resp = urllib2.urlopen(serv_req)
	>>> reader = csv.DictReader(serv_resp)
	>>> for row in reader:
	...     print row
	... 
	{'Name': 'Portugal', 'Contact': 'info@zeitgeistportugal.org', 'Link': 'http://www.zeitgeistportugal.org/', 'Location': 'Portugal', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Porto', 'Contact': 'porto@zeitgeistportugal.org', 'Link': 'http://porto.zeitgeistportugal.org', 'Location': 'Porto, Portugal', 'Type': 'Region', 'Icon': '2'}
	{'Name': 'Lisboa', 'Contact': 'lisboa@zeitgeistportugal.org', 'Link': 'http://lisboa.zeitgeistportugal.org', 'Location': 'Lisbon, Portugal', 'Type': 'Region', 'Icon': '2'}
	{'Name': '\xd0\x91\xd1\x8a\xd0\xbb\xd0\xb3\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f', 'Contact': 'zgeistbg@gmail.com', 'Link': 'http://thezeitgeistmovement.bg/', 'Location': 'Bulgaria', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Colombia', 'Contact': 'zeitgeistcolombia@gmail.com', 'Link': 'http://www.zeitgeistcolombia.com/', 'Location': 'Colombia', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Spain', 'Contact': 'info@movimientozeitgeist.org', 'Link': 'http://movimientozeitgeist.org/', 'Location': 'Spain', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Belgium', 'Contact': 'info@thezeitgeistmovement.be', 'Link': 'http://www.thezeitgeistmovement.be/', 'Location': 'Belgium', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Argentina', 'Contact': 'comunicacion@zeitgeistargentina.com', 'Link': 'http://www.zeitgeistargentina.com', 'Location': 'Argentina', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Mexico', 'Contact': 'contacto@zeitgeist.com.mx', 'Link': 'http://www.zeitgeist.com.mx', 'Location': 'Mexico', 'Type': 'Country', 'Icon': '1'}
	{'Name': 'Denmark', 'Contact': 'info@thezeitgeistmovement.dk', 'Link': 'http://thezeitgeistmovement.dk/', 'Location': 'Denmark', 'Type': 'Country', 'Icon': '1'}

Here is the python API if we want to be able to write to this as well.

	☺  svn checkout http://fusion-tables-client-python.googlecode.com/svn/trunk/ fusion-tables-client-python-read-only

You can also return the JSON directly into the javascript

	☺  curl https://www.google.com/fusiontables/api/query?sql=SELECT%20*%20FROM%203027809&jsonCallback=foo                                                                          ""
	[1] 4031
	☺  Type,Name,Link,Contact,Location,Icon                                                                                                                                         ""
	Country,Portugal,http://www.zeitgeistportugal.org/,info@zeitgeistportugal.org,Portugal,1
	Region,Porto,http://porto.zeitgeistportugal.org,porto@zeitgeistportugal.org,"Porto, Portugal",2
	Region,Lisboa,http://lisboa.zeitgeistportugal.org,lisboa@zeitgeistportugal.org,"Lisbon, Portugal",2
	Country,България,http://thezeitgeistmovement.bg/,zgeistbg@gmail.com,Bulgaria,1
	Country,Colombia,http://www.zeitgeistcolombia.com/,zeitgeistcolombia@gmail.com,Colombia,1
	Country,Spain,http://movimientozeitgeist.org/,info@movimientozeitgeist.org,Spain,1
	Country,Belgium,http://www.thezeitgeistmovement.be/,info@thezeitgeistmovement.be,Belgium,1
	Country,Argentina,http://www.zeitgeistargentina.com,comunicacion@zeitgeistargentina.com,Argentina,1
	Country,Mexico,http://www.zeitgeist.com.mx,contacto@zeitgeist.com.mx,Mexico,1
	Country,Denmark,http://thezeitgeistmovement.dk/,info@thezeitgeistmovement.dk,Denmark,1
	...

[API Documentation](https://developers.google.com/fusiontables/docs/developers_reference)

We can also use Javascript directly, like:

	    > var geoCodes = { "type": "FeatureCollection","features": [{ "type": "Feature","geometry": {"type": "Point", "coordinates": [-122.4211908, 37.7564513]},"properties": { "id": "2950648771574984913", "accuracyInMeters": 80, "timeStamp": 1309323032, "reverseGeocode": "San Francisco, CA, USA", "photoUrl": "https://www.google.com/latitude/apps/badge/api?type=photo&photo=uuRL2jABAAA.9fWeRzNpS-tdX0cqHxxclg.7zdBNW-Rb634EIkOgyO8sw", "photoWidth": 96, "photoHeight": 96, "placardUrl": "https://www.google.com/latitude/apps/badge/api?type=photo_placard&photo=uuRL2jABAAA.9fWeRzNpS-tdX0cqHxxclg.7zdBNW-Rb634EIkOgyO8sw&moving=true&stale=true&lod=1&format=png", "placardWidth": 56, "placardHeight": 59}}]};

	    > console.log(geoCodes.features);
	    [ Object
	      geometry: Object
	      properties: Object
	      type: "Feature"
	      __proto__: Object

then to go into the features Object, you can do this:

	     > var features = geoCodes.features;
	     > for(var i = arr.length - 1; i >= 0; --i) { 
			var o = arr[i]; 
			var geometry = o.geometry;
			var properties = o.properties; 
			console.log(geometry, properties);
		};

	     > geometry
	      Object
	      coordinates: Array[2]
	      type: "Point"
	      __proto__: Object

	     > 	properties
			Object
			accuracyInMeters: 80
			id: "2950648771574984913"
			photoHeight: 96
			photoUrl: "https://www.google.com/latitude/apps/badge/api?type=photo&photo=uuRL2jABAAA.9fWeRzNpS-tdX0cqHxxclg.7zdBNW-Rb634EIkOgyO8sw"
			photoWidth: 96
			placardHeight: 59
			placardUrl: "https://www.google.com/latitude/apps/badge/api?type=photo_placard&photo=uuRL2jABAAA.9fWeRzNpS-tdX0cqHxxclg.7zdBNW-Rb634EIkOgyO8sw&moving=true&stale=true&lod=1&format=png"
			placardWidth: 56
			reverseGeocode: "San Francisco, CA, USA"
			timeStamp: 1309323032
			__proto__: Object

	     > console.log(geometry.coordinates[0]);
	       -122.4211908

JSON

	> $.getJSON(target_url + '&jsonCallback=?', function(json) { 
	   console.log(json.table.cols);
	   var row, feature, atts = {}, features = [];
	   var cols = json.table.cols; // column names
	   for(var i = 0; i < json.table.rows.length; i++) {
	     row = json.table.rows[i];
	     atts = {};
	     for (var j = 0; j < row.length; j++) {
	         if (typeof row[j] === "object") {
	           console.log((row[j]));
	         } else {
	           atts[cols[j]] = row[j];
	         }
	     }
	    console.log(json.table.rows[i]);
	   }
	 });
	
#GeoCoding

Once we have the data, we can now Geocode it, using GeoPy:

	>>> from geopy import geocoders
	>>> g = geocoders.Google('_API_KEY')
	>>> chapters = g.geocode("Porto, Portugal", exactly_one=False) 
	>>> print chapters
	[(u'Oporto, Portugal', (41.1650559, -8.602816)), (u'Francisco de S\xe1 Carneiro Airport (OPO), 4470-558, Portugal', (41.2411264, -8.6802374))]
	>>> print chapters[0]
	(u'Oporto, Portugal', (41.1650559, -8.602816))
	
#Using nodejs within python

`scraper.js`

    var jsdom = require('jsdom');

    var args = process.argv.slice(2),
        html = unescape(args[0]),
        parser = unescape(args[1]);

    jsdom.env({
        html: html,
        scripts: ['./jquery.js']
    }, function(err, window){
        $ = window.jQuery;
        try{
            eval(parser);
        }catch(e){console.log({error: e});}
    });

`foo.py`
    
	import urllib2
    import commands

    html = urllib2.urlopen('http://google.com').read();
    parser = """var title = $('#hplogo').attr('alt');
    console.log({'title':title});
    """
    content = commands.getoutput('node ./scraper.js %s %s' % 
                                 (urllib2.quote(html), urllib2.quote(parser)))

	>>> "{title: 'Google'}"

#Update Tue 27 Mar 2012 10:14:00 CEST

* the map.zmgc.net is functioning and needs to be integrated into this project
* use redis to log data from the map stats and then push this into itools, it will be more efficient

#Gitlib and Gitolite

* use gitolite/gitlib to make communication between remote nodes more efficient
* use riak cluster to store the user sessions and then clone these across the nodes

#Project.py

A core project website has members


#Freebase
Access to data, the Open Source way.

	from apiclient import discovery
	from apiclient import model
	import json

	DEVELOPER_KEY = 'YOUR-KEY-GOES-HERE'

	model.JsonModel.alt_param = ""
	freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
	query = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]

	response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
	for planet in response['result']:
		print planet['name']


#Video and Audio Widget
[http://nkhine.github.com/zPlayer/](http://nkhine.github.com/zPlayer/) - this has a 3 tabs - 'Video', 'Audio' , 'Both' where the data comes from the 'ul' list

[https://github.com/nkhine/zPlayer/blob/gh-pages/index.html#L219](https://github.com/nkhine/zPlayer/blob/gh-pages/index.html#L219)

Need to extend the player so that it works with youtube videos, so that we have a custom jPlayer widget, to link to a
playlist, see the [https://developers.google.com/youtube/2.0/reference#youtube_data_api_tag_media:content](https://developers.google.com/youtube/2.0/reference#youtube_data_api_tag_media:content)

Here is the example for TZMOfficialChannel [http://gdata.youtube.com/feeds/api/users/TZMOfficialChannel/uploads?v=2&alt=jsonc](http://gdata.youtube.com/feeds/api/users/TZMOfficialChannel/uploads?v=2&alt=jsonc)

Using jPlayer it is not possible (well i have not found a way yet) to stream the YouTube video, although [http://www.jplayer.org/latest/jPlayer-tester/](http://www.jplayer.org/latest/jPlayer-tester/) there is an option 'FLV Test from YouTube'

Read data from 3 different files for each of the tab lists, based on:

* tab-1, 'Global' will pull the playlist from global-media.json file (http://gdata.youtube.com/feeds/api/users/TZMOfficialChannel/uploads?v=2&alt=jsonc)
 
* tab-2, 'Regional' will pull the playlist from regional-media.json file (http://gdata.youtube.com/feeds/api/users/ZeitgeistMovementUK/uploads?v=2&alt=jsonc)

* tab-3, 'Local' will pull the playlist local-media.json file (this will contain links to different video/audio suppliers and formats)


the idea behind this will be so that when the zplayer widget is installed on the users' website it will be able to pull data from all these data sources.

each tab should list the first 5 items and be combined withhttp://msjolund.github.com/autobrowse/ so that you get a scroller that loads the next items.

here is an example:
[http://www.briskelderlaw.com/VideoVault/examples/player-multiple-playlists.html?iframe=true&width=720&height=100%](http://www.briskelderlaw.com/VideoVault/examples/player-multiple-playlists.html?iframe=true&width=720&height=100%) of a youtube player with a playlist using jquery where the categories in our case will be the TABS.

Not all sources would come from YouTube, so the javascript code will need to take care of this and load the correct player depending on the content.
		
#Home Page

##Globe
When a logged in user adds content, the home page 'globe' will rotate and centre on the lat/lon position, which is worked out from the user's IP address or the location the user has chosen to use within their preferences and we animate a specific colour 'circle' depending on what the user has added.
We then use the jQuery 'Transfer Effect' from this point to the 'div' where the new item's Title and Short Description are displayed in real time.
