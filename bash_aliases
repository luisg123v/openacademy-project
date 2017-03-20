# A symbolic link in ~/.bash_aliases is pointing to this file

# Aliases to facilitate dealing with odoo parameters
alias odoo='~/odoo/odoo.py -d odoo_curso --addons-path=~/my-modules,~/odoo/addons'
# Not always using --log-level=debug, too much unnecessary info
alias odoo_wdemo='~/odoo/odoo.py -d wdemo --addons-path=~/my-modules,~/odoo/addons -u openacademy --test-enable --stop-after-init'

# causes ls to display one result per line
alias ls='ls -1'

cd ~
