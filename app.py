import re
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import gradio as gr

# Load the T5 model and tokenizer
model_name = "bilal521/t5-youtube-summarizer"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Clean and summarize text
def summarize_with_t5(text):
    input_text = "summarize: " + text.strip()
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    summary_ids = model.generate(
        inputs,
        max_length=256,
        min_length=80,
        num_beams=5,
        length_penalty=2.0,
        no_repeat_ngram_size=3,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Extract video ID from any YouTube URL
def extract_video_id(url):
    regex = r"(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?|shorts)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None

# Optional: Clean up repeated or spammy lines
def clean_transcript(text):
    lines = text.split("\n")
    seen = set()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.lower() in seen:
            continue
        if re.match(r'https?:\/\/', line):
            continue
        seen.add(line.lower())
        clean_lines.append(line)
    return " ".join(clean_lines)

# Main logic to fetch transcript and summarize
def get_youtube_transcript(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Could not extract video ID. Please check the URL."

    try:
        yt = YouTubeTranscriptApi()
        transcript = yt.fetch(video_id, languages=['en'])

        formatter = TextFormatter()
        raw_text = formatter.format_transcript(transcript)
        cleaned_text = clean_transcript(raw_text)
        summary = summarize_with_t5(cleaned_text)
        return summary

    except Exception as e:
        return f"Error occurred: {e}"

# Gradio UI
demo = gr.Interface(
    fn=get_youtube_transcript,
    inputs=[gr.Textbox(label="YouTube Video URL", lines=1, placeholder="Paste your YouTube URL here")],
    outputs=[gr.Textbox(label="Summarized Transcript", lines=10)],
    title="YouTube Video Summarizer",
    description="This app extracts and summarizes the transcript of a YouTube video using a fine-tuned T5 model."
)

demo.launch()
