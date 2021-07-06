# NVOIP_Reports
A TelegramBot module for NVOIP reports

## Instalation
First you will need to download or clone this repository and put it on the modules folder.
Then edit the following files:

keys.json
```json
{
    "tt_key": "YOURNVOIPTOKEN",
    "data": {
        "some_user": {
            "username": "UserNameHere"
        },
        "some_user": {
            "username": "UserNameHere"
        }
    }
}
```

list.txt
```text
Put in this file just one line, it will be displayed as many times as you have open tickets in your department, and it also has keywords :)
```
## KeyWords List
KeyWords for model.txt
```python
{balance} = Returns balance
```

## Usage
Send a message in the chat as in the following example:
```
/n user
```
Where the `user` is equals to one of the values you put on the keys.json attribute.

And you're done! The bot will reply with all the data you wanted.
