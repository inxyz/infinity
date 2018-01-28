#### GPG encrypted secret files

**env.sh** example:
```bash
#!/usr/bin/env bash

export DOCKER_USERNAME='username'
export DOCKER_PASSWORD='password'

```

##### Travis  

For travis we can use file encrypted with just a passphrase.
Generate encrypted travis password and encrypt file with `gpg`
```bash
travis encrypt keys_password=password123 --add
gpg -c ./keys/env_travis.sh

# and type your password you've generated with travis cli
```

Use your `keys_password` env variable during the travis run:  
```bash
echo ${keys_password} | gpg --passphrase-fd 0  ./keys/env_travis.sh.gpg
source ./keys/env_travis.sh
```

--- 

##### Users
For users we can use both passphrase and users public keys.  
 - Import others public key:
```bash
curl https://api.github.com/users/<GITHUB_USERNAME>/gpg_keys | jq -r ".[0].raw_key" | gpg --import -
```

 - Encrypt file with those keys
```bash
gpg -e -r <email> -r <email> ./keys/env.sh 
```

 - Decrypt and use (one of private keys should be installed on host):
 ```bash
gpg ./keys/env.sh.gpg
source ./keys/env.sh
```

