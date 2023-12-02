# httparam2json
Process URL parameters and convert them to JSON format.

#### Usage:

```bash
$ python3 httparam2json.py - jq "fname=firstname&lname=lastname" 
{
  "fname": "firstname",
  "lname": "lastname"
}
```