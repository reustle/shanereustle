---
title: Backing Up Your Meteor.com Database
---

Meteor provides a nifty little hosting service for your projects through the `meteor deploy` command. Once deployed, your app gets its own mongo instance where it stores all of your data. Creating a backup of this remote instance is pretty straight forward, once we have the connection credentials.

You can run `meteor mongo your-app.meteor.com` to connect to the mongo instance your app is using and execute commands, but adding `--url` to the end returns only your connection string. Using this login is tricky, as it is only valid for 60 seconds. The command below will take care of this for you by grabbing the remote  mongo credentials and then create a backup using mongodump.

<pre>
meteor mongo your-app.meteor.com --url | awk -F'[:/@]' '{print "mongodump --host "$6" --db "$8" --port "$7" --username "$4" --password "$5}' | sh
</pre>

You'll see the output of the mongodump command as it creates the backup folder and pulls down a copy of each collection. If you need to restore a copy of the database, connect to remote instance and clear everything out, and then use mongorestore to revert back.

