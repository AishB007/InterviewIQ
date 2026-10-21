import gradio as gr
from questions import get_question, state

with gr.Blocks( theme=gr.themes.Soft(), title="InterviewIQ" ) as demo:
    gr.Markdown(""" # 🎯 InterviewIQ ### AI-Powered Interview Practice Platform Practise interview questions, review feedback, and track your progress. """)

    with gr.Row():
        with gr.Column(scale=6): 
            gr.Markdown("## 🎤 Current Question") 
            question_display = gr.Markdown(get_question()) 
            answer_box = gr.Textbox( label="Your Answer", placeholder="Type your interview answer here...", lines=7 )

            submit_button = gr.Button( "Submit Answer", variant="primary" ) 
            
            gr.Markdown("## 📝 Feedback Panel") 
            feedback_panel = gr.Markdown( "Your evaluation feedback will appear here." )

        # RIGHT COLUMN
        with gr.Column(scale=5):
            gr.Markdown("## 📊 Live Scorecard")
            scorecard = gr.Markdown( "No answers submitted yet." )
            gr.Markdown("## 🧭 Interview Coach")
            coach_input = gr.Textbox( label="Ask Your Coach", placeholder="How am I doing so far?", lines=3 )
            coach_button = gr.Button("Ask Coach")
            coach_output = gr.Markdown( "Ask a question about your interview progress." )

    gr.Markdown("---") 
    gr.Markdown("## 📄 Final Interview Report")

    report_button = gr.Button( "Generate Final Report", variant="primary" )



if __name__ == "__main__": 
    demo.launch()