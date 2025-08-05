# 🎥 YouTube Video Summarizer with T5

This is a simple and powerful web app that summarizes the **transcript of any YouTube video** using a fine-tuned T5 transformer model. Built with Python, Hugging Face Transformers, and Gradio.

## ✨ Features

- Accepts any YouTube URL
- Extracts transcript using `youtube-transcript-api`
- Cleans and deduplicates the transcript
- Summarizes it using a fine-tuned T5 model
- User-friendly web UI powered by Gradio

## 📦 Requirements
requirements.txt:

torch
transformers
gradio
youtube-transcript-api
protobuf
sentencepiece

## 🤖 Model Info
The summarization is powered by:

bilal521/t5-youtube-summarizer — A fine-tuned T5 model for summarizing YouTube transcripts.
<b> citation: </b>                                   <br>
@misc{t5ytsummarizer2025,                            <br>
  title={T5 YouTube Transcript Summarizer},          <br>
  author={Muhammad Bilal Yousaf},                    <br>
  year={2025},                                       <br>
  howpublished={\url{https://huggingface.co/bilal521/t5-youtube-summarizer}},
}

## 📸 UI Preview

You can take a screenshot after you launch the app and replace the link above.

## 🛡️ License
MIT License


---
