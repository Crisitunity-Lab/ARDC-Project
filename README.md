# Crisis Management
Crisis management is a complex problem to which responses have real world impacts. Often much of the data that is provided in a crsis is unstructured making it hard to retieve meaningful information; information that could be used by authorities and agencies to provide better services and care. This project aims to take unstructured data, generated during a crisis, and generate meaningful information. 

## Dataset
For this project the CrisisLexT26 dataset was used (Olteanu et al, 2015). This data is publicly available from [here](https://github.com/sajao/CrisisLex/blob/master/releases/CrisisLexT26-v1.0.zip?raw=true).The dataset contains ~28,000 labelled tweets from 26 crisis events that occurred in 2012 and 2013. Tweets were labelled with informativeness, information type and information source using crowdsourcing.

## Large Language Models
Large language models (LLMs) are deep learning systems designed to mimic humans. LLMs are trained on a large corpus of text and are designed to predict the next word in a sentence, or paragraph. This allows them to communicate fluently with humans in a natural way. LLM’s have performed well on MBA exams and have performed at, or near, the passing threshold for the United States Medical Licencing Exam (Kung, 2023; Terwiesch, 2023). This suggests LLMs can perform well on complex tasks. 

There are a number of open-source LLM's available to the public. In this project Llama2, GPT-3.5 and Falcon-7B were evaluated. Llama2-7B-Chat was chosen to perform experimentation.

### Llama2-7B-Chat
The Llama2-7B-Chat LLM is part of a family of open-source large language models created by Meta (Touvron et al, 2023). The Llama2 models were made available to the public in July 2023. Llama2-7B-Chat is a 7 billion parameter model pretrained on 2 trillion tokens of data from publicly available sources.

## Prompting
Responses from LLMs are only as good as the prompts they are given. There are multiple prompting techniques and they include:

- Zero-shot prompting,
- Few-shot prompting
- Chain of Thought prompting

For this project zero-shot prompting was used.

### Zero-Shot Prompting
LLMs can respond to prompts despite having never seen the instructions before. When the prompt contains no other information other than the instruction, this is called _zero-shot prompting_. As an example:

_Prompt_

> Can you give me the sentiment for the following snippet:
>
> Nothing lower than fire looters: NSW cops http://t.co/ftZYbYy8u2

_Response_

> Negative

In this example the LLM has been asked to provide a sentiment score without any further information, or context. This is zero-shot prompting at work.

## Experiments
### Experiment 1 - Informativeness

### Experiment 2 - Information Type

### Experiment 3 - Crisis Type

### Experiment 4 - Country

## Installing


## References
Kung, T. H., Cheatham, M., Medenilla, A., Sillos, C., De Leon, L., Elepaño, C., Madriaga, M., Aggabao, R., Diaz-Candido, G., Maningo, J., & Tseng, V. (2023) Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models. _PLOS Digital Health_, 2(2), [https://doi.org/10.1371/journal.pdig.0000198](https://doi.org/10.1371/journal.pdig.0000198)

Olteanu, A., Vieweg, S., & Castillo, C. (2015) What to Expect When the Unexpected Happens: Social Media Communications Across Crises. _In Proceedings of the ACM 2015 Conference on Computer Supported Cooperative Work and Social Computing (CSCW '15)_. ACM, Vancouver, BC, Canada. 

Terwiesch, C. (2023) Would Chat GPT Get a Wharton MBA? A Prediction Based on Its Performance in the Operations Management Course. Mack Institute for Innovation Management at the Wharton School, _University of Pennsylvania_ [https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/01/Christian-Terwiesch-Chat-GTP-1.24.pdf](https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/01/Christian-Terwiesch-Chat-GTP-1.24.pdf)

Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., Bikel, D., Blecher, L., Ferrer, C. C., Chen, M., Cucurull, G., Esiobu, D., Fernandes, J., Fu, J., Fu, W., … Goyal, N. (2023) Llama 2: Open Foundation and Fine-Tuned Chat Models. [https://doi.org/10.48550/arxiv.2307.09288](https://doi.org/10.48550/arxiv.2307.09288)