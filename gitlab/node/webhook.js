var http = require('http');
var qs = require('querystring');
var fs = require('fs');
var nodemailer = require('nodemailer');
var spawn = require('child_process').spawn;
var format = require('string-format');

var bat = require.resolve('./run_update.bat');

function sendMail(payload, callback) {
	let transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com',
        port: 465,
        secure: true, // true for 465, false for other ports
        auth: {
            user: "rodicarogozin", // generated ethereal user
            pass: "***" // generated ethereal password
        }
    });
	
	var head = format(fs.readFileSync("mail_head.html", "utf8"), {
		author_name: payload.sender.login,
		repository_url: payload.repository.html_url,
		repository_name: payload.repository.full_name
	});
	
	var commits = "<ul>";
	for (var i in payload.commits) {
		var cmt = format(fs.readFileSync("commit.html", "utf8"), {
			author_url: payload.sender.html_url,
			avatar_url: payload.sender.avatar_url,
			author_username: payload.commits[i].author.username,
			commit_url: payload.commits[i].url,
			commit_message: payload.commits[i].message,
			repo_url: payload.repository.html_url,
			commit_time: payload.commits[i].timestamp,
			commit_sha: payload.commits[i].id.substring(0, 7),
			commit_id: payload.commits[i].id
		});
		commits += cmt;
	}
	
	var footer = fs.readFileSync("mail_footer.html", "utf8");
	
	let mailOptions = {
        from: '"GitLab sync 😎" <no-reply@scratch-ai.win>', // sender address
        to: payload.commits[0].author.email, // list of receivers
        subject: 'Your commits have been synced to GitLab ✔', // Subject line
        html: head + commits + footer
    };
	
	console.log(JSON.stringify(mailOptions));
	
	transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log(error);
        }
		callback();
    });
}

http.createServer(function (req, res) {
	
	if (req.url.startsWith("/commit.wsx")) {
		
		var body = '';
		req.on("data", function(data) {
			body += data;
		});
		req.on("end", function() {
			var data = qs.parse(body);
			var payload = JSON.parse(decodeURI(data.payload));
			
			if (req.headers["x-github-event"] == "push") {
				var ls = spawn(bat);
				ls.stdout.on('data', function (data) {
					console.log(data);
				});
				ls.on("exit", function() {
					sendMail(payload, function() {
						res.end();
					});
				});
			}
		});
	}
	else 
	{
		res.write("<h1>That's a 404!</h1>");
		res.end(); //end the response
	}
}).listen(80); //the server object listens on port 8080