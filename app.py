from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_video():
    idea = request.form.get('idea')
    
    # هنا يمكننا الاتصال بـ Gemini API (أو أي ذكاء اصطناعي نصي) لتوليد النص بناءً على الفكرة
    # للتبسيط، سنستخدم الفكرة مباشرة كنص للفيديو
    video_text = idea
    
    # إنشاء الفيديو باستخدام FFmpeg (نص أبيض على خلفية سوداء)
    output_file = "output.mp4"
    command = [
        "ffmpeg",
        "-f", "lavfi", "-i", "color=c=black:s=1280x720:d=5", # خلفية سوداء 5 ثواني
        "-vf", f"drawtext=text='{video_text}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
        "-y", output_file
    ]
    
    # تشغيل الأمر
    subprocess.run(command)
    
    # إرسال الفيديو للمستخدم
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
