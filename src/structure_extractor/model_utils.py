from langchain import PromptTemplate, LLMChain
import transformers
from transformers import AutoTokenizer
import torch


def download_hf_model(model="meta/Llama-2-7b-chat-hf"):
    tokenizer = AutoTokenizer.from_pretrained(model)

    pipeline = transformers.pipeline(
        "text-generation", #task
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
        max_length=1000,
        do_sample=True,
        top_k=10,

        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id
        )

    return pipeline


def get_prompt_template(instruction="", system_prompt=None):

    # Prompt Template Formatting
    start_instruction, end_instruction = "[INST]", "[/INST]"
    start_sys_prompt, end_sys_prompt = "<>\n", "\n<>\n\n"

    if not(system_prompt):
        system_prompt = "You are a helpful, respectful and honest assistant. Always answer as helpfully as "\
        "possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, "\
        "toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and "\
        "positive in nature. "\
        "If a question does not make any sense, or is not factually coherent, explain why instead of answering "\
        "something not correct. If you don't know the answer to a question, please don't share false information."
    
    system_prompt_template = start_sys_prompt + system_prompt + end_sys_prompt
    prompt_template = start_instruction + system_prompt_template + instruction + end_instruction
    
    return prompt_template


def generate_answer(text, prompt, llm):
    # Create prompt template
    prompt = PromptTemplate(template=prompt, input_variables=['text'])

    # Return answer from LLM
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    output = llm_chain.run(text)

    return output