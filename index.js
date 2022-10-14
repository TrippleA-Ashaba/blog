const express = require("express");
const path = require("path");
const _ = require("lodash");

const homeStartingContent = `Lorem ipsum dolor sit amet consectetur adipisicing elit. Sed, impedit. Veniam corrupti magnam aperiam officia numquam explicabo modi inventore est aliquam sed! Quia laborum distinctio illo nobis at, corrupti recusandae! Convallis aenean et tortor at risus viverra adipiscing at. Nunc non blandit massa enim nec dui. Faucibus interdum posuere lorem ipsum dolor sit amet consectetur adipiscing. Malesuada fames ac turpis egestas maecenas. Vel risus commodo viverra maecenas accumsan lacus. Nulla facilisi nullam vehicula ipsum a arcu cursus vitae congue. Consectetur purus ut faucibus pulvinar elementum integer enim.`;

const aboutContent = `Vel risus commodo viverra maecenas accumsan lacus. Id aliquet lectus proin nibh nisl condimentum id. Id nibh tortor id aliquet lectus proin. Sit amet nisl purus in mollis nunc. Nunc eget lorem dolor sed viverra ipsum nunc aliquet`;

const contactContent = `Convallis aenean et tortor at risus viverra adipiscing at. Vel risus commodo viverra maecenas accumsan lacus. Nulla facilisi nullam vehicula ipsum a arcu cursus vitae congue. Consectetur purus ut faucibus pulvinar elementum integer enim.`;

// app
const app = express();

// global variables
const posts = [];

// configuration
app.set("view engine", "pug");
app.set("views", path.join(__dirname, "views"));

// middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

// Routes
app.get("/", (req, res) => {
	res.render("index", {
		title: "Daily Journal",
		message: homeStartingContent,
		posts: posts,
	});
});

app.get("/about", (req, res) => {
	res.render("about", { title: "Daily Journal: About", message: aboutContent });
});

app.get("/contact", (req, res) => {
	res.render("contact", { title: "Daily Journal: Contact", message: contactContent });
});

app.get("/compose", (req, res) => {
	res.render("compose", { title: "Daily Journal: Compose" });
});

app.post("/compose", (req, res) => {
	const post = {
		title: req.body.postTitle,
		content: req.body.postBody,
	};
	posts.push(post);
	res.redirect("/");
});

app.get("/posts/:postName", (req, res) => {
	const requestedTitle = _.lowerCase(req.params.postName);
	posts.forEach(function (post) {
		const storedTitle = _.lowerCase(post.title);
		if (storedTitle == requestedTitle) {
			res.render("post", {
				postTitle: post.title,
				postContent: post.content,
			});
		}
	});
});

// unresolved routes
app.get("*", (req, res) => {
	res.send(
		"<h1 style='text-align:center; font-size:70px; margin-top:5%;'>🥹🥹🥹😭<br>Page Unavailable</h1>"
	);
});

//server
app.listen(3000, console.log("😊👂👂👂👂🔊🔊......... 3000!!"));
