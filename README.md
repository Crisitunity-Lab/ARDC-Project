# Crisis Management
Crisis management is a complex problem to which responses have real world impacts. Often much of the data that is provided in a crsis is unstructured making it hard to retieve meaningful information; information that could be used by authorities and agencies to provide better services and care. This project aims to take unstructured data, generated during a crisis, and generate meaningful information. 

## Dataset
For this project the CrisisLexT26 dataset was used (Olteanu et al, 2015). This data is publicly available from [here](https://github.com/sajao/CrisisLex/blob/master/releases/CrisisLexT26-v1.0.zip?raw=true).The dataset contains ~28,000 labelled tweets from 26 crisis events that occurred in 2012 and 2013. Tweets were labelled with informativeness, information type and information source through crowdsourcing.

### Data Cleansing
To prepare data for analysis several tasks were undertaken to enrich and clean the data obtained. The cleansing tasks undertaken were:

- Country Codes: Adding country codes to the dataset,
- Crisis Type: Adding crisis type to the dataset, and
- Tweet Length: Removing rows with a message length less than 5 words, although this is configurable when running [data_utils.combine_csv_files](https://github.com/Crisitunity-Lab/ARDC-Project/blob/163d4c3a586200bf334c7311dff5b548218abc53/src/structure_extractor/data_utils.py#L17).

### Data Collection Example
An example of how to collect the data source can be found [here](https://github.com/Crisitunity-Lab/ARDC-Project/blob/main/Notebooks/Example_Data_Collection.ipynb).

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
As part of this project four experiments were run. These experiments investigated how well a LLM would perform labelling data and generating relevant metadata. The following fields were investigated:

- **Informativeness**,
- **Information Type**,
- **Crisis Type**, and
- **Country Impacted**.

These experiments are explored in more detail below.

### Experiment 1 - Informativeness
As the X platform is an open space for communication, not all messages about a crisis are informative or related. The informativeness field aims to provide a measure of how related to, and informative about, the crisis the message is. The four labels in the original dataset were:

- Related and informative: the message contains information that aids understanding of the crisis,
- Related - but not informative: the message refers to the crisis event but does not contain
information that aids understanding of the crisis,
- Not related: the tweet is not related to the crisis, and
- Not applicable: informativeness not provided by the labeller

As part of this project the Llama2-7B-Chat model was asked to categorise messages with one of the three labels provided in the source dataset.

The overall accuracy of results from the informativeness experiment was **52.79%** with the _Related and informative_ category performing better than the others with a precision of **65.47%** and a recall of **67.23%**. The other categories performed worse with a precision of ~30%.

### Experiment 2 - Information Type
The information type categorisation conveys information about the subject of the message. There are 7 labels in the source dataset. These are:

- Affected individuals: includes information about missing people, people trapped or
injured, casualties and reports from those directly impacted by the crisis,
- Caution and advice: includes information on how to prepare for the crisis and safety
warnings and advice during, and after, the event,
- Donations and volunteering: includes information about how to donate money, goods
or services and how best to help the community through volunteering,
- Infrastructure and utilities: includes information about damage to buildings, traffic
conditions and available medical services,
- Other Useful Information: includes the location of emergency responders and
information on conditions (e.g., flood level, smoke, wind speed),
- Sympathy and support: includes messages of support from the those impacted and
gratitude for assistance, and
- Not labeled [sic]: no information type provided by the labeller.

As with experiment 1, the Llama2-7B-Chat model was asked to categorise messages with one of the seven labels provided in the source dataset. 

The overall accuracy of results from the information type experiment was **46.77%**. Again results varied across each of the labels. _Affected individuals_ had a recall of close to 80% but had a precision of just above 40%, whilst the labels _Donations and volunteering_ and _Symapthy and support_ had the opposite results.

### Experiment 3 - Crisis Type
Each of the records in the dataset are about a crisis event that occurred at some point in 2012 or 2013. The crisis types in the dataset included:

- Wildfire,
- Earthquake,
- Typhoon, and
- Flood.

The crisis type is different to the two prior experiments in that the data is metadata rather than crowd-sourced labels. In this experiment the model was asked to decided what type of crisis the message was about.

The overall accuracy of results from the crisis type experiment was **69.48%**. For identifying the crisis type the model performed reasonably well on most crisis types with exceptions being Fire ([2013 Brazil nightclub fire](https://en.wikipedia.org/wiki/Kiss_nightclub_fire)) and Explosion ([2013 fertiliser explosion](https://en.wikipedia.org/wiki/West_Fertilizer_Company_explosion) in West Texas). In both these case the model struggled, especially when trying to standardise on a term. Is it an explosion, or a blast, or a factory explosion. This issue was also evident with typhoons which are also known as hurricanes and tropical cyclones, or by the name given to them. This impacted the results.

### Experiment 4 - Country
The metadata of country impacted by thye crisis event was also captured and investigated. The source dataset covered crisis events in 14 countries with the United States having the most messages followed by the Philippines.

The overall accuracy for country was **64.93%** but the variability of results between countries was high. For example, messages about events in the United States of America struggled. Often this was due to the the model, despite being asked explicitly for a country, returning a US state, or a city name. 

## Notes
The results contained here provide a view on how LLMs perform with little, or no, context. Whilst experimental results for some of the metadata fields these should be viewed with caution. The project team is not privvy to the data used to train the Llama2-7b-Chat model. The model is (most probably) aware of the crisis events researched here and this may have impacted the results. If the model was asked to identify the crisis type, or country impacted, for a more recent crisis event how would it perform? The project team can not say and more investigation into this is required.

The model used in this experiment was largely dictated by access to compute and memory resources. Larger LLMs exist and may perform better on this task.

The experiments were run using the pre-trained Llama2-7b-Chat model. The model used for experimentation was **not** trained on crisis specific data. This may be useful at improving results, especially where bespoke categories are required.

The information contained in this repository is the work of the project team.

## Running
An example on how to run the experiments is shown in [this](https://github.com/Crisitunity-Lab/ARDC-Project/blob/main/Notebooks/Example_Run_Experiments.ipynb) notebook. To run the notebook code users will need a [Hugging Face](https://huggingface.co/welcome) account and have been given permission from Meta to use the Llama2 models. Persmission can be granted by filling out [this](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) form.

## References
Kung, T. H., Cheatham, M., Medenilla, A., Sillos, C., De Leon, L., Elepaño, C., Madriaga, M., Aggabao, R., Diaz-Candido, G., Maningo, J., & Tseng, V. (2023) Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models. _PLOS Digital Health_, 2(2), [https://doi.org/10.1371/journal.pdig.0000198](https://doi.org/10.1371/journal.pdig.0000198)

Olteanu, A., Vieweg, S., & Castillo, C. (2015) What to Expect When the Unexpected Happens: Social Media Communications Across Crises. _In Proceedings of the ACM 2015 Conference on Computer Supported Cooperative Work and Social Computing (CSCW '15)_. ACM, Vancouver, BC, Canada. 

Terwiesch, C. (2023) Would Chat GPT Get a Wharton MBA? A Prediction Based on Its Performance in the Operations Management Course. Mack Institute for Innovation Management at the Wharton School, _University of Pennsylvania_ [https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/01/Christian-Terwiesch-Chat-GTP-1.24.pdf](https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/01/Christian-Terwiesch-Chat-GTP-1.24.pdf)

Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., Bikel, D., Blecher, L., Ferrer, C. C., Chen, M., Cucurull, G., Esiobu, D., Fernandes, J., Fu, J., Fu, W., … Goyal, N. (2023) Llama 2: Open Foundation and Fine-Tuned Chat Models. [https://doi.org/10.48550/arxiv.2307.09288](https://doi.org/10.48550/arxiv.2307.09288)