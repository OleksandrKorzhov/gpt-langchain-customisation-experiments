## Usage
1. (**ALREADY DONE - BY THE REPO AUTHORS**) Prepare sample data for playing with. Use [data preparation](./data_preparation.ipynb) notebook to complete this step;
2. Run the minimal [search by embeddings](./search_by_embeddings.ipynb) example to understand the overall logic of producing GPT response;
3. Run [content chunking](./content_chunking.ipynb) notebook to understand the difference and benefits of using GPT for text preparation before using it for Q/A;
4. Run [search by embeddings from db](./search_by_embeddings_from_db.ipynb) notebook to use near-production search solution that uses LLM and embeddings;
5. Run [prompt with stored embeddings](prompt_with_embeddings.ipynb) notebook to see a complete solution with question answering based on the Pinecone vector DB;

## Key moments to focus on during development
- Retrieval of the most relevant to the user provided prompt information;
- Transformation of the user provided prompt with a prompt template;

## Useful references

- Customised bot implementation from a third party author https://replit.com/@OleksandrKorzho/Custom-Chatbot#process.py;
- Spark by examples (Pandas) https://sparkbyexamples.com/pandas;
- Q&A Bot with Llama-Index and LangChain (Google colab) https://colab.research.google.com/drive/1JYTczk-4D86XNn0GTaXux5yi2-LfoIPd?usp=sharing#scrollTo=GW1tTw2VeWgS;
- OpenAI playground https://platform.openai.com/playground?mode=complete;
- OpenAI fine tuning https://platform.openai.com/docs/guides/fine-tuning;
- OpenAI cookbook https://github.com/openai/openai-cookbook;
- OpenAI semantic text search https://github.com/openai/openai-cookbook/blob/main/examples/Semantic_text_search_using_embeddings.ipynb;
- Amazon food reviews dataset https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews?resource=download;
- Using Vector Databases for Embeddings Search - https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb;
- Techniques to improve reliability - https://github.com/openai/openai-cookbook/blob/c5b9be87548d67f9409bcbac0deccfa0fe30d5c6/techniques_to_improve_reliability.md;
- Question Answering with Langchain, Qdrant and OpenAI - https://github.com/openai/openai-cookbook/blob/0d006b2cf2c6c46b9e91f6f0669031e715caac73/examples/vector_databases/qdrant/QA_with_Langchain_Qdrant_and_OpenAI.ipynb;
- Choosing the Right Approach: Embedding or Fine-tuning for GPT API-based Software with Proprietary Content https://www.linkedin.com/pulse/choosing-right-approach-embedding-fine-tuning-gpt-api-based-tong/;
- Fine Tuning GPT-3: Building a Custom Q&A Bot Using Embeddings https://www.mlq.ai/fine-tuning-gpt-3-question-answer-bot/;

## Information sources
- Text embedding for NLP task, text clusterization and integration with Pinecone https://betterprogramming.pub/openais-embedding-model-with-vector-database-b69014f04433;
- OpenAI topic - Splitting / Chunking Large input text for Summarisation (greater than 4096 tokens….) https://community.openai.com/t/splitting-chunking-large-input-text-for-summarisation-greater-than-4096-tokens/18494;
- Summarizing books with human feedback https://openai.com/research/summarizing-books;
- OpenAI topic - How to prevent Open AI from making up an answer https://community.openai.com/t/how-to-prevent-open-ai-from-making-up-an-answer/18370;

## Tools

### Youtube transcript
- Youtube transcript https://chrome.google.com/webstore/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli;
- Introducing Whisper (transcripts a video and groups text by the context) https://openai.com/research/whisper;
- MLQ Academy: Build a YouTube Video Assistant Using Whisper & GPT-3 https://www.mlq.ai/youtube-video-assistant-whisper-gpt-3/;

- Library for summarization https://github.com/daveshap/RecursiveSummarizer;
- Azure OpenAI service https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview;

### Vector databases & vector search
- Pinecone https://docs.pinecone.io/docs/openai;
- Supabase support for vector search https://supabase.com/docs/guides/getting-started/openai/vector-search;

### Data presentation apps
- https://streamlit.io/;
