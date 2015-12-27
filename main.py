import os

run = False

#lvl 1 easy mode
user_answers_easy={"lvl1":[], "lvl2":[], "lvl3":[]}
#sentince
lvl1_easy = """
	Basic {1} are the backbone of any HTML document.
	You'll see these elements in the source {2} for all web pages, following the {3} declaration, which is on the first line of the page.
	The doctype specifies which {4} of (X)HTML that page is using.
	Elements comprising the contents of a Web page are placed between the opening <html> tag and the closing </html> tag.
	The <html> element is also known as the root element.
"""
#correct answers
lvl1_easy_answers = ["elements", "code", "doctype", "version"]


#lvl 2 easy mode
#sentince
lvl2_easy = """
	Metadata contains information about the {1}.
	This includes information about styles, scripts and {2} to help software (search engines, browsers, etc.) use and render the page.
	Metadata for {3} and scripts may be defined in the page or {4} to another file that has the information.
"""
#correct answers
lvl2_easy_answers = ["code", "data", "styles", "link"]
#lvl 3 easy mode
#sentince
lvl3_easy = """
	Content sectioning elements allow you to {1} the document content into {2} pieces.
	Use the sectioning elements to create a broad outline for your {3} content,
	including header and {4} navigation, and heading elements to identify sections of content.
"""
#correct answers
lvl3_easy_answers = ["organize", "logical", "page", "footer"]

easy_aswers = {"lvl1": lvl1_easy_answers,"lvl2": lvl2_easy_answers, "lvl3": lvl3_easy_answers}

easy_sentences = [lvl1_easy, lvl2_easy, lvl3_easy]

#lvl 1 mediam mode
user_answers_mediam={"lvl1":[], "lvl2":[], "lvl3":[]}
#sentince
lvl1_mediam = """
	Basic {1} are the backbone of any HTML document.
	You'll see these elements in the source {2} for all web pages, following the {3} declaration, which is on the first line of the page.
	The doctype specifies which {4} of (X)HTML that page is using.
	Elements comprising the contents of a Web page are placed between the opening <html> tag and the closing </html> tag.
	The <html> element is also known as the {5} element.
"""
#correct answers
lvl1_mediam_answers = ["elements", "code", "doctype", "version", "root"]
#lvl 2 mediam mode
#sentince
lvl2_mediam = """
	Metadata contains information about the {1}.
	This includes information about styles, scripts and {2} to help software (search engines, browsers, etc.) use and render the page.
	Metadata for {3} and scripts may be defined in the page or {4} to another {5} that has the information.
"""
#correct answers
lvl2_mediam_answers = ["code", "data", "styles", "link", "file"]
#lvl 3 mediam mode
#sentince
lvl3_mediam = """
	Content sectioning elements allow you to {1} the document content into {2} pieces.
	Use the sectioning elements to create a broad outline for your {3} content,
	including header and {4} navigation, and heading elements to {5} sections of content.
"""
#correct answers
lvl3_mediam_answers = ["organize", "logical", "page", "footer", "identify"]

mediam_answers = {"lvl1": lvl1_mediam_answers,"lvl2": lvl2_mediam_answers, "lvl3": lvl3_mediam_answers}

mediam_sentences = [lvl1_mediam, lvl2_mediam, lvl3_mediam]

#lvl 1 hard mode
user_answers_hard={"lvl1":[], "lvl2":[], "lvl3":[]}
#sentince
lvl1_hard = """
	Basic {1} are the backbone of any HTML document.
	You'll see these elements in the source {2} for all web pages, following the {3} declaration, which is on the first line of the page.
	The doctype specifies which {4} of (X)HTML that page is using.
	Elements comprising the contents of a Web page are placed between the opening <html> tag and the closing </html> tag.
	The <html> {5} is also known as the {6} element.
"""
#correct answers
lvl1_hard_answers = ["elements", "code", "doctype", "version", "element", "root"]
#lvl 2 hard mode
#sentince
lvl2_hard = """
	Metadata contains information about the {1}.
	This includes information about styles, scripts and {2} to help software (search engines, browsers, etc.) use and render the page.
	Metadata for {3} and scripts may be defined in the page or {4} to another {5} that has the {6}.
"""
#correct answers
lvl2_hard_answers = ["code", "data", "styles", "link", "file", "information"]
#lvl 3 hard mode
#sentince
lvl3_hard = """
	Content sectioning elements allow you to {1} the document content into {2} pieces.
	Use the sectioning elements to create a broad outline for your {3} content,
	including header and {4} navigation, and heading elements to {5} sections of {6}.
"""
#correct answers
lvl3_hard_answers = ["organize", "logical", "page", "footer", "identify", "content"]

hard_answers = {"lvl1": lvl1_hard_answers,"lvl2": lvl2_hard_answers, "lvl3": lvl3_hard_answers}

hard_sentences = [lvl1_hard, lvl2_hard, lvl3_hard]

#cod that makes evrything work

while run == False:
	game_mode = raw_input("type your game mode hear e m h: ")
	os.system("clear")
	if game_mode == "e":
		run = True
		for lvl in range(1, 4):
			print  easy_sentences[lvl - 1]
			for blank in range(1, 5):
				while True:
					answer = raw_input("what is your answer for blank %s: " % blank)
					if answer == easy_aswers["lvl%s" % lvl][blank - 1]:
						user_answers_easy["lvl%s" % lvl].append({str(blank): answer})
						easy_sentences[lvl - 1] = easy_sentences[lvl - 1].replace("{%s}" % blank, easy_aswers["lvl%s" % lvl][blank - 1])
						os.system("clear")
						print easy_sentences[lvl - 1]
						break
			os.system("clear")
			print "good job you beat the game on easy mode"

	if game_mode == "m":
		run = True
		for lvl in range(1, 4):
			print  mediam_sentences[lvl - 1]
			for blank in range(1, 6):
				while True:
					answer = raw_input("what is your answer for blank %s: " % blank)
					print mediam_answers["lvl%s" % lvl][blank -1]
					print user_answers_mediam["lvl%s" % lvl]
					print blank
					if answer == mediam_answers["lvl%s" % lvl][blank - 1]:
						user_answers_mediam["lvl%s" % lvl].append({str(blank): answer})
						mediam_sentences[lvl - 1] = mediam_sentences[lvl - 1].replace("{%s}" % blank, mediam_answers["lvl%s" % lvl][blank - 1])
						os.system("clear")
						print mediam_sentences[lvl - 1]
						break
			os.system("clear")
			print "good job you beat the game on medium mode"

	if game_mode == "h":
		run = True
		for lvl in range(1, 4):
			print  hard_sentences[lvl - 1]
			for blank in range(1, 7):
				while True:
					answer = raw_input("what is your answer for blank %s: " % blank)
					print hard_answers["lvl%s" % lvl][blank -1]
					print user_answers_hard["lvl%s" % lvl]
					print blank
					if answer == hard_answers["lvl%s" % lvl][blank - 1]:
						user_answers_hard["lvl%s" % lvl].append({str(blank): answer})
						hard_sentences[lvl - 1] = hard_sentences[lvl - 1].replace("{%s}" % blank, hard_answers["lvl%s" % lvl][blank - 1])
						os.system("clear")
						print hard_sentences[lvl - 1]
						break
			os.system("clear")
			print "good job you beat the game on hard mode"