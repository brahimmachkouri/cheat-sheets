## Multipass CheatSheet - 20231205 - BM

| Commande | Description |
| --- | --- |
| `multipass find` | Affiche la liste des images disponibles que vous pouvez installer. |
| `multipass launch --name myvm` | Crée une nouvelle machine virtuelle avec le nom "myvm". |
| `multipass launch focal --name myvm` | Crée une nouvelle machine virtuelle de la version "focal" d'Ubuntu avec le nom "myvm". |
| `multipass shell myvm` | Ouvre un shell interactif dans la machine virtuelle "myvm". |
| `multipass exec myvm -- /bin/bash -c "sudo apt update && sudo apt upgrade"` | Exécute une commande à l'intérieur de la machine virtuelle pour mettre à jour les paquets. |
| `multipass stop myvm` | Arrête la machine virtuelle "myvm". |
| `multipass start myvm` | Démarre la machine virtuelle "myvm". |
| `multipass delete myvm` | Supprime la machine virtuelle "myvm". |
| `multipass purge` | Supprime définitivement toutes les machines virtuelles supprimées pour libérer de l'espace disque. |
| `multipass list` | Affiche la liste des machines virtuelles en cours d'exécution. |
| `multipass launch --cpus 2 --mem 2G --disk 10G` | Crée une nouvelle machine virtuelle avec une configuration spécifique en termes de CPU, mémoire et espace disque. |
| `multipass transfer fichier.txt myvm:` | Transfère le fichier "fichier.txt" depuis l'hôte vers le répertoire home de la machine virtuelle "myvm". |
| `multipass mount $HOME myvm` | Montre le répertoire home de l'hôte dans la machine virtuelle "myvm". |
| `multipass mount /home/sub/dev myvm:/home/ubuntu/dev` | Montre le répertoire /home/sub/dev de l'hôte dans /home/ubuntu/dev de la machine virtuelle "myvm". |
| `multipass launch --name myvm --mount /home/sub/codeigniter:/home/ubuntu/codeigniter` | Crée une nouvelle machine virtuelle "myvm" et monte le répertoire /home/sub/codeigniter de l'hôte dans /home/ubuntu/codeigniter de la machine virtuelle. |
| `multipass info myvm` | Affiche des informations détaillées sur la machine virtuelle "myvm", y compris les points de montage actifs. |
| `multipass help` | Affiche des informations d'aide sur l'utilisation de Multipass. |
| `multipass version` | Affiche la version de Multipass. |
| `multipass restart myvm` | Redémarre la machine virtuelle "myvm". |
| `multipass suspend myvm` | Met en pause la machine virtuelle "myvm". |
| `multipass resume myvm` | Reprend l'exécution de la machine virtuelle "myvm" depuis la pause. |
| `multipass info --all` | Affiche des informations détaillées sur toutes les machines virtuelles, y compris celles arrêtées. |
| `multipass alias add myalias myvm` | Crée un alias "myalias" pour la machine virtuelle "myvm". |
| `multipass alias list` | Affiche la liste des alias créés pour les machines virtuelles. |
| `multipass shell myalias` | Ouvre un shell interactif dans la machine virtuelle "myvm" en utilisant l'alias "myalias". |
