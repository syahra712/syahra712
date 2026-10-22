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
**Latest merge:** [Use UTF-8 for stdout so non-ASCII results can be printed on Windows](https://github.com/GoogleCloudPlatform/professional-services-data-validator/pull/1853) in **GoogleCloudPlatform/professional-services-data-validator** · 2026-10-22
<!-- latest ends -->

<!-- merged starts -->
| Project | ⭐ | Area | What I fixed |
|---|:--:|---|---|
| [**docling-project/docling**](https://github.com/docling-project/docling) | `69k` | document AI · VLMs | [Coerce MLX bfloat16 logprobs to float in VlmPredictionToken](https://github.com/docling-project/docling/pull/4005) |
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | `62k` | LLM gateway · billing | [Don't retire a completed batch from cost recovery while output_file_id is lagging](https://github.com/BerriAI/litellm/pull/37715) |
| [**sshuttle/sshuttle**](https://github.com/sshuttle/sshuttle) | `14k` | networking · firewalls | [pf exclusions ignored under a wider include since rules became quick](https://github.com/sshuttle/sshuttle/pull/1270)<br/>[Skip hostwatch when the server has no os.fork](https://github.com/sshuttle/sshuttle/pull/1271)<br/>[Keep the tunnel up when a DNS or UDP reply cannot be sent](https://github.com/sshuttle/sshuttle/pull/1273)<br/>[Drop the zone id of a link-local nameserver from nft rules](https://github.com/sshuttle/sshuttle/pull/1272) |
| [**tox-dev/tox**](https://github.com/tox-dev/tox) | `4k` | Python test tooling | [Keep the packaging backend captured with --no-capture](https://github.com/tox-dev/tox/pull/4164) |
| [**aboutcode-org/scancode-toolkit**](https://github.com/aboutcode-org/scancode-toolkit) | `2.7k` | license compliance | [Cap pluggy below 1.7.0](https://github.com/aboutcode-org/scancode-toolkit/pull/5364) |
| [**cuthbertLab/music21**](https://github.com/cuthbertLab/music21) | `2.6k` |  | [(AI) Read MusicXML octave-change in transpose without diatonic](https://github.com/cuthbertLab/music21/pull/2086)<br/>[(AI) Order TimespanTree.allParts() by the source score](https://github.com/cuthbertLab/music21/pull/2089) |
| [**fossasia/voxbento**](https://github.com/fossasia/voxbento) | `1.5k` | web API · access control | [Scope admin transcript routes to the requested event](https://github.com/fossasia/voxbento/pull/813) |
| [**fossasia/veditor**](https://github.com/fossasia/veditor) | `1.5k` |  | [Show app INFO logs so the dev verification link is visible](https://github.com/fossasia/veditor/pull/317) |
| [**mpmath/mpmath**](https://github.com/mpmath/mpmath) | `1.2k` | arbitrary precision | [Flip rounding direction when negating in mpf_gamma(type=3) (fixes iv.loggamma)](https://github.com/mpmath/mpmath/pull/1204) |
| [**apache/iceberg-python**](https://github.com/apache/iceberg-python) | `1.2k` | apache | [Preserve null maps when projecting a map of structs](https://github.com/apache/iceberg-python/pull/4118) |
| [**pymc-devs/pytensor**](https://github.com/pymc-devs/pytensor) | `648` | ai | [Index 0-d MakeVector inputs instead of calling .item() in numba](https://github.com/pymc-devs/pytensor/pull/2503) |
| [**mozilla/bugbug**](https://github.com/mozilla/bugbug) | `576` | agentic ai | [Keep full comment text when rendering Phabricator revisions](https://github.com/mozilla/bugbug/pull/7197) |
| [**GoogleCloudPlatform/professional-services-data-validator**](https://github.com/GoogleCloudPlatform/professional-services-data-validator) | `532` |  | [Convert Impala connection options given as strings to their real types](https://github.com/GoogleCloudPlatform/professional-services-data-validator/pull/1852)<br/>[Use UTF-8 for stdout so non-ASCII results can be printed on Windows](https://github.com/GoogleCloudPlatform/professional-services-data-validator/pull/1853) |
| [**fortran-lang/fortls**](https://github.com/fortran-lang/fortls) | `346` | fortls | [Handle mixed quotes in find_paren_match](https://github.com/fortran-lang/fortls/pull/569) |
| [**openSUSE/opi**](https://github.com/openSUSE/opi) | `290` | cli | [Fetch file:// and $releasever gpgkeys correctly when asking to keep a key](https://github.com/openSUSE/opi/pull/227) |
| [**getmail6/getmail6**](https://github.com/getmail6/getmail6) | `168` |  | [#277: malformed POP3 UIDL/LIST aborts only the affected account](https://github.com/getmail6/getmail6/pull/284) |
| [**openfoodfacts/open-prices**](https://github.com/openfoodfacts/open-prices) | `110` | crowdsourcing | [API: accept `location_id` when updating a proof](https://github.com/openfoodfacts/open-prices/pull/1476) |
| [**pypa/distlib**](https://github.com/pypa/distlib) | `65` | Python packaging | [Use the Python-2.0.1 SPDX license identifier](https://github.com/pypa/distlib/pull/276) |
| [**ga4gh/vrs-python**](https://github.com/ga4gh/vrs-python) | `64` | bioinformatics | [Reject trailing input in beacon, gnomAD and SPDI translators](https://github.com/ga4gh/vrs-python/pull/670) |
| [**SciTools/ncdata**](https://github.com/SciTools/ncdata) | `16` |  | [Replace deprecated licence config in pyproject.toml](https://github.com/SciTools/ncdata/pull/268) |
| [**konflux-ci/rpm-lockfile-prototype**](https://github.com/konflux-ci/rpm-lockfile-prototype) | `16` |  | [Handle registry port numbers in image specs](https://github.com/konflux-ci/rpm-lockfile-prototype/pull/184)<br/>[Add --tls-verify option for skopeo calls](https://github.com/konflux-ci/rpm-lockfile-prototype/pull/186) |
| [**plone/plone.event**](https://github.com/plone/plone.event) | `5` |  | [Pass re.MULTILINE to re.sub as flags, not as count](https://github.com/plone/plone.event/pull/71) |
| [**apache/solr-orbit**](https://github.com/apache/solr-orbit) | `3` | apache | [Build the Docker image on Python 3.13, inside requires-python](https://github.com/apache/solr-orbit/pull/126)<br/>[Page through collections with SolrClient.search in create-workload](https://github.com/apache/solr-orbit/pull/125)<br/>[Restore metrics.metrics_store_class so solr-orbit stop works again](https://github.com/apache/solr-orbit/pull/124)<br/>[Create ClusterEnvironmentInfo so --telemetry cluster-environment-info works](https://github.com/apache/solr-orbit/pull/135)<br/>[Add a make licenses target that generates THIRD_PARTY.md](https://github.com/apache/solr-orbit/pull/133) |
<!-- merged ends -->

<!-- review starts -->
<details>
<summary><b>🕐 In review: 87 PRs across 74 projects</b>, including markitdown, mem0, litellm, crewAI, agno, dspy, smolagents…</summary>

<br/>

| Project | ⭐ | Fix |
|---|:--:|---|
| [microsoft/markitdown](https://github.com/microsoft/markitdown/pull/2302) | `192k` | Refactor ImageConverter to reuse llm_caption helper |
| [mem0ai/mem0](https://github.com/mem0ai/mem0/pull/7001) | `68k` | Dispatch add_embeddings on actual signature |
| [BerriAI/litellm](https://github.com/BerriAI/litellm/pull/45952) | `62k` | Route GPT-5.4+ function-tool calls through the Responses API |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI/pull/8040) | `60k` | Opt-in deferred tool loading via Responses tool search |
| [agno-agi/agno](https://github.com/agno-agi/agno/pull/9596) | `43k` | Chain exception causes in tool, model, and vectordb error paths |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy/pull/10227) | `39k` | Add sort_keys=True to tool call/result JSON serialization |
| [huggingface/smolagents](https://github.com/huggingface/smolagents/pull/2950) | `30k` | Accept AgentImage/AgentAudio state values for image/audio tool inputs |
| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot/pull/34806) | `16k` | Tools: param_unpack.py: support param.pck files with defaults |
| [sympy/sympy](https://github.com/sympy/sympy/pull/30318) | `15k` | Annotate sympy/physics/quantum/qft.py |
| [pyro-ppl/pyro](https://github.com/pyro-ppl/pyro/pull/3500) | `9.1k` | Restore deep_getattr in pyro.infer.autoguide.utils |
| [arrow-py/arrow](https://github.com/arrow-py/arrow/pull/1391) | `9.1k` | Use calendar months for humanize month and quarter granularity |
| [marshmallow-code/marshmallow](https://github.com/marshmallow-code/marshmallow/pull/3073) | `7.2k` | Reject leading/trailing hyphen in the last domain label in validate.Email |

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
