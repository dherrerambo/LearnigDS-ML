# Comandos GIT

## Eliminar un archivo de la historia
git filter-branch --tree-filter 'rm -f anexos/ANEXOS-EAPB.zip' HEAD


## cambio de crlf
https://es.stackoverflow.com/questions/320373/por-qu%C3%A9-al-hacer-git-add-me-dice-lf-will-be-replaced-by-crlf-the-file-will-h
$ git config --global core.autocrlf false


git revert --no-commit HEAD~3..
git commit -m "your message regarding reverting the multiple commits"


# Revertir cambios en VsCode
- CTRL + SHIFT + P
- Look for: git revert
- Hit Enter