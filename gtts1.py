import gtts

TEXT = "Nel mezzo del cammin di nostra vita, mi ritrovai in una selva oscura, che la diritta via era smarrita!"

tts = gtts.gTTS(text=TEXT, lang="it")
tts.save("nel_mezzo.mp3")