Pybot is a simple irc bot that evaluates expressions and says results.

Install
=======

```
$git clone https://github.com/potix2/pybot.git
$cd pybot
$pip install -r requirements.txt
```

Usage
=====

Execute following command,

```
$python pybot/irc.py <channel_name>
```

then Pybot will connect irc.freenode.net and join the channel as 'pybot'.

In the room if you say like that:

```
>1 + 2
```

then pybot say '3'.

License
=======
MIT License

Author
======
Katsunori Kanda `<potix2@gmail.com>`
