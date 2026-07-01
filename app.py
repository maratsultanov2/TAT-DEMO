"""
TAT-7 Divergence Trace — Gradio Demo
Запуск: python app.py
"""

import gradio as gr
import numpy as np

def compute_divergence(text, phase):
    """Имитация divergence trace для демонстрации."""
    phase_map = {
        "Стабильность": 0.001,
        "Сомнение": 1.000,
        "Конфликт": 2.000,
        "Синтез": 3.000,
        "Новая стабильность": 4.000
    }
    base = phase_map.get(phase, 0.0)
    noise = np.random.normal(0, 0.01)
    divergence = base + noise
    
    if divergence < 0.10:
        status = "✅ Consolidate"
    elif divergence < 0.30:
        status = "⚠️ Escalated (5 heads)"
    else:
        status = "🛑 Withhold (7 heads)"
    
    return f"{divergence:.4f}", status

with gr.Blocks(title="TAT-7 Divergence Trace") as demo:
    gr.Markdown("# TAT-7 Divergence Trace Demo")
    gr.Markdown("Введите текст и выберите ожидаемую семантическую фазу.")
    
    with gr.Row():
        text_input = gr.Textbox(label="Текст для анализа", lines=4)
        phase_input = gr.Dropdown(
            choices=["Стабильность", "Сомнение", "Конфликт", "Синтез", "Новая стабильность"],
            label="Семантическая фаза"
        )
    
    with gr.Row():
        divergence_output = gr.Textbox(label="Divergence")
        status_output = gr.Textbox(label="Gate Decision")
    
    btn = gr.Button("Анализировать")
    btn.click(compute_divergence, inputs=[text_input, phase_input], outputs=[divergence_output, status_output])

if __name__ == "__main__":
    demo.launch()
