# 🎥 YouTube Video Summarizer with T5 Transformer

This is a simple and powerful web app that summarizes the **transcript of any YouTube video** using a fine-tuned T5 transformer model. Built with Python, Hugging Face Transformers, and Gradio.

## ✨ Features

- Accepts any YouTube URL
- Extracts transcript using `youtube-transcript-api`
- Cleans and deduplicates the transcript
- Summarizes it using a fine-tuned T5 model
- User-friendly web UI powered by Gradio

## 📦 Requirements
requirements.txt:              

torch                            <br>
transformers                     <br>
gradio                           <br>
youtube-transcript-api           <br>
protobuf                         <br>
sentencepiece                    

## ⚠️ Deployment Note
This app uses the youtube-transcript-api to fetch transcripts directly from YouTube.
Due to network restrictions on free Hugging Face Spaces, the app may throw a Failed to resolve 'www.youtube.com' error when deployed there.

<b> Workarounds:  </b>

Run the app locally using python app.py

Or deploy on platforms that allow outbound internet (e.g., Gradio Hosted, Inference Endpoints, or Render)

## 🤖 Model Info
The summarization is powered by:

bilal521/t5-youtube-summarizer — A fine-tuned T5 model for summarizing YouTube transcripts.

<br>
<b> citation: </b>                                   <br>

@misc{t5ytsummarizer2025,

  title={T5 YouTube Transcript Summarizer},
  
  author={Muhammad Bilal Yousaf},
  
  year={2025},
  
  howpublished={\url{https://huggingface.co/bilal521/t5-youtube-summarizer}},
}


## 📸 UI Preview

You can take a screenshot after you launch the app and replace the link above.

## 🛡️ License
None. This is a personal project for learning purpose and can be used by anyone.


---
