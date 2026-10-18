<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/syahra712/syahra712/main/assets/hero-light.svg"/>
  <img src="https://raw.githubusercontent.com/syahra712/syahra712/main/assets/hero.svg" alt="Syed Ahnaf Raza — AI Engineer and open-source contributor" width="100%"/>
</picture>

<a href="https://syedahnafrazaportfolio-syed-ahnaf-razas-projects.vercel.app"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>
<a href="https://linkedin.com/in/syed-ahnaf-raza"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="https://github.com/pulls?q=is%3Apr+author%3Asyahra712+-user%3Asyahra712+-user%3Aahnaf-lab"><img src="https://img.shields.io/badge/Upstream_PRs-see_all-3fb950?style=for-the-badge&logo=github&logoColor=white" alt="All upstream pull requests"/></a>

</div>

I build **RAG systems, LLM agents and data pipelines**, and I fix bugs in the open-source projects they're built on. When something breaks in a library I depend on, I read the source, reproduce the bug and send the fix upstream.

**Right now**
- 🔧 Contributing across the **LLM-agent stack**, with PRs open in litellm, crewAI, dspy, smolagents, mem0 and markitdown
- 🔤 Building [**urdukit**](https://github.com/syahra712/urdukit), NLP tooling for Urdu, a language that 230M people speak and few libraries support
- 💼 PMO @ [VentureDive](https://pk.linkedin.com/company/venturedive) · Software Engineering @ Bahria University

---

## 🔧 Merged upstream

<!-- latest starts -->
**Latest merge:** [Keep full comment text when rendering Phabricator revisions](https://github.com/mozilla/bugbug/pull/7197) in **mozilla/bugbug** · 2026-10-17
<!-- latest ends -->

<!-- merged starts -->
| Project | ⭐ | Area | What I fixed |
|---|:--:|---|---|
| [**docling-project/docling**](https://github.com/docling-project/docling) | `69k` | document AI · VLMs | [Coerce MLX bfloat16 logprobs to float in VlmPredictionToken](https://github.com/docling-project/docling/pull/4005) |
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | `61k` | LLM gateway · billing | [Don't retire a completed batch from cost recovery while output_file_id is lagging](https://github.com/BerriAI/litellm/pull/37715) |
| [**sshuttle/sshuttle**](https://github.com/sshuttle/sshuttle) | `14k` | networking · firewalls | [pf exclusions ignored under a wider include since rules became quick](https://github.com/sshuttle/sshuttle/pull/1270)<br/>[Skip hostwatch when the server has no os.fork](https://github.com/sshuttle/sshuttle/pull/1271)<br/>[Keep the tunnel up when a DNS or UDP reply cannot be sent](https://github.com/sshuttle/sshuttle/pull/1273)<br/>[Drop the zone id of a link-local nameserver from nft rules](https://github.com/sshuttle/sshuttle/pull/1272) |
| [**tox-dev/tox**](https://github.com/tox-dev/tox) | `4k` | Python test tooling | [Keep the packaging backend captured with --no-capture](https://github.com/tox-dev/tox/pull/4164) |
| [**aboutcode-org/scancode-toolkit**](https://github.com/aboutcode-org/scancode-toolkit) | `2.6k` | license compliance | [Cap pluggy below 1.7.0](https://github.com/aboutcode-org/scancode-toolkit/pull/5364) |
| [**fossasia/voxbento**](https://github.com/fossasia/voxbento) | `1.5k` | web API · access control | [Scope admin transcript routes to the requested event](https://github.com/fossasia/voxbento/pull/813) |
| [**mozilla/bugbug**](https://github.com/mozilla/bugbug) | `576` | agentic ai | [Keep full comment text when rendering Phabricator revisions](https://github.com/mozilla/bugbug/pull/7197) |
| [**pypa/distlib**](https://github.com/pypa/distlib) | `65` | Python packaging | [Use the Python-2.0.1 SPDX license identifier](https://github.com/pypa/distlib/pull/276) |
| [**apache/solr-orbit**](https://github.com/apache/solr-orbit) | `3` | apache | [Build the Docker image on Python 3.13, inside requires-python](https://github.com/apache/solr-orbit/pull/126)<br/>[Page through collections with SolrClient.search in create-workload](https://github.com/apache/solr-orbit/pull/125)<br/>[Restore metrics.metrics_store_class so solr-orbit stop works again](https://github.com/apache/solr-orbit/pull/124) |
<!-- merged ends -->

<!-- review starts -->
<details>
<summary><b>🕐 In review: 69 PRs across 53 projects</b>, including markitdown, mem0, litellm, crewAI, agno, dspy, smolagents…</summary>

<br/>

| Project | ⭐ | Fix |
|---|:--:|---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown/pull/2302) | `191k` | Refactor ImageConverter to reuse llm_caption helper |
| [mem0ai/mem0](https://github.com/mem0ai/mem0/pull/7001) | `67k` | Dispatch add_embeddings on actual signature |
| [BerriAI/litellm](https://github.com/BerriAI/litellm/pull/45952) | `61k` | Route GPT-5.4+ function-tool calls through the Responses API |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI/pull/8040) | `60k` | Opt-in deferred tool loading via Responses tool search |
| [agno-agi/agno](https://github.com/agno-agi/agno/pull/9596) | `43k` | Chain exception causes in tool, model, and vectordb error paths |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy/pull/10227) | `39k` | Add sort_keys=True to tool call/result JSON serialization |
| [huggingface/smolagents](https://github.com/huggingface/smolagents/pull/2950) | `30k` | Accept AgentImage/AgentAudio state values for image/audio tool inputs |
| [sympy/sympy](https://github.com/sympy/sympy/pull/30318) | `15k` | Annotate sympy/physics/quantum/qft.py |
| [pyro-ppl/pyro](https://github.com/pyro-ppl/pyro/pull/3500) | `9.1k` | Restore deep_getattr in pyro.infer.autoguide.utils |
| [marshmallow-code/marshmallow](https://github.com/marshmallow-code/marshmallow/pull/3073) | `7.2k` | Reject leading/trailing hyphen in the last domain label in validate.Email |
| [containers/podman-compose](https://github.com/containers/podman-compose/pull/1581) | `6.2k` | Support passing --scale multiple times |
| [skorch-dev/skorch](https://github.com/skorch-dev/skorch/pull/1175) | `6.2k` | Restore best score in PassthroughScoring when continuing training |

<sub>[See every open PR →](https://github.com/pulls?q=is%3Apr%20is%3Aopen%20author%3Asyahra712%20-user%3Aahnaf-lab%20-user%3Asyahra712)</sub>

</details>
<!-- review ends -->

<sub>This section updates itself every 6 hours from the GitHub API. See [`scripts/update.py`](scripts/update.py).</sub>

---

## 🚀 Things I've built

<table>
<tr>
<td width="50%" valign="top">

### [🔤 urdukit](https://github.com/syahra712/urdukit)
A zero-dependency **Urdu NLP toolkit** for normalization, tokenization, stopwords, stemming and Roman-Urdu transliteration. `pip install` and go: no TensorFlow and no model downloads.

`Python` `NLP` `low-resource languages`

</td>
<td width="50%" valign="top">

### [🛠️ HizmatAI](https://github.com/syahra712/aihack-hizmatai)
A two-sided **agentic booking platform** for Pakistan's informal economy. A 6-agent Google ADK pipeline on Gemini connects customers with home-service providers in Urdu, Roman-Urdu and English.

`multi-agent` `Flutter` `FastAPI` `React`

</td>
</tr>
<tr>
<td valign="top">

### [🕸️ Graph-Augmented Research Agent](https://github.com/syahra712/Graph-Augmented-Intelligent-Research-Agent)
A research agent that goes beyond plain RAG: it combines embedding similarity with **co-citation and bibliographic coupling** for literature search, gap analysis, plagiarism detection and citation formatting.

`RAG` `citation graphs` `LLM agents`

</td>
<td valign="top">

### [🌫️ AQI forecasting pipeline](https://github.com/syahra712/AQI10Pearls)
An end-to-end **MLOps** pipeline. Scheduled ingestion feeds a Hopsworks feature store, models retrain automatically, and a live dashboard shows the forecasts, all running on GitHub Actions.

`MLOps` `feature store` `time series`

</td>
</tr>
<tr>
<td valign="top">

### [🫥 hiddenink](https://github.com/syahra712/hiddenink)
*Find the ink you can't see.* It detects and cleans invisible Unicode, homoglyphs and container metadata, and decides for each occurrence whether the character is a hidden mark or real content.

`Python` `text security` `zero-dep`

</td>
<td valign="top">

### [🌳 yaadain](https://github.com/syahra712/yaadain)
A living **family tree for Urdu-speaking elders with memory loss**. It's an offline-first Flutter app built for reminiscence and simulated-presence therapy.

`Flutter` `Dart` `health`

</td>
</tr>
</table>

<sub>More: [BridgeSign](https://github.com/syahra712/AIProject-BridgeSign) (real-time ASL recognition) · [EcoViz](https://github.com/syahra712/DataVisualzationEcoViz) (emissions dashboards and model benchmark) · [TumorVision](https://github.com/syahra712/PEC-Hackathon) (MRI classification with Grad-CAM) · [AES-RSA](https://github.com/syahra712/AES-RSA) (hybrid encryption service)</sub>

---

## 🎖️ Experience & credentials

| | |
|---|---|
| 💼 **Experience** | PMO @ **VentureDive** · Technical APM @ **CodeAvenue** · RAG / LLM systems @ **Sybrid** · ML pipelines @ **10Pearls** |
| 🏆 **Awards** | Regional Winner, **National Agentic AI Hackathon** |
| 📜 **Certs** | Oracle **Generative AI Professional** · Stanford **ML Specialization** · Microsoft **PL-300** · Google **Project Management** |
| 🌱 **Leadership** | Hult Prize Campus Director · VP, Bahria University Development Society |

## 🛠️ Stack

| | |
|---|---|
| **AI / ML** | PyTorch · TensorFlow · Hugging Face · LangChain · Google ADK · spaCy · RAG · LLM agents |
| **Languages** | Python · TypeScript · JavaScript · Dart · SQL |
| **Build & ship** | FastAPI · React · Next.js · Flutter · Docker · MongoDB · GitHub Actions · n8n |

---

<div align="center">
<sub>Open to <b>AI/ML engineering</b> and <b>applied AI project management</b> roles · If you maintain a Python project and have a gnarly bug, I'd like to hear about it.</sub>
</div>
