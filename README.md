# httparam2json

#### Install:



#### Usage:

```bash
$ python3 httparam2json.py "fname=firstname&lname=lastname" | jq
{
  "fname": "firstname",
  "lname": "lastname"
}
```