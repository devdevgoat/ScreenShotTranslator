# Notes
On an M1 mack I had to install this first:
```
brew install libjpeg 
```
then I could run the following. Trying to install these with pipenv causes errors.
```
pipenv shell
pip install pillow
pip install typing-extensions
```

Change the deminsions on line 8 to the location of your game window on your screen. The format is Left, Top, Right, Bottom. So (0,0,100,100) would be the top 100 square pixels on the left side of the screen. 

# Setup:

You'll neeed to rename .env.example to '.env' and add your [OpenAI API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)

# Run:
```
python windowwatcher.py
```