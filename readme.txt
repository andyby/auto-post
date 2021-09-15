1. downlown hugo command line utility from below url
    https://github.com/gohugoio/hugo/releases

2. init the project, in the same folder with hugo run:
    ./hugo new site random_adage

3. install a theme, cd to themes directory, run:
    git clone https://github.com/vimux/mainroad

4. enamle the downloaded theme, edit config.toml
    theme = "mainroad"

5. write auto-post.py script and run

6. hugo server -D to check result 

7. hugo -D to build final static site to public folder

8. git init to initiate repo, 
   git add . and git commit -m 'init commit'

git push https://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@github.com/andyby/auto-post.git

   git remote add origin https://github.com/andyby/auto-post.git

   git push origin master