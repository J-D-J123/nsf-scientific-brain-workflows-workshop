# 📗 Pre-Workshop Notebook 2: Working with Larger Research Datasets
## Scientific Workflows for Brain and Behavioral Research
### National Science Foundation Supported Learning Initiative (Award No. OAC-2417875)

---

## 📋 Set Up Your Profile
*Run the cell below to record your progress.*
# PROFILE SYNC
student_name = "Your Name"
institution = "Your University/Organization"
active_notebook = "Notebook 02 — Larger Datasets and Simultaneous Processing"

print(f"✅ Profile synced for {student_name} ({institution})")
print(f"Current notebook: {active_notebook}")
---

## 🤖 Using AI Tools to Build Your Workflow ("Ask → Build → Document")

As a **Workflow Designer** working with larger datasets, your main challenge is managing how much data your analysis can handle at once. AI tools are excellent at writing individual calculations, but they sometimes ignore the fact that loading too much data at once can slow your computer down or cause it to run out of working memory.

When using the **Ask → Build → Document** cycle in this notebook, pay attention to how much memory your analysis is using, and ask the AI to explain any steps that involve loading large amounts of data.

---
## 🧠 Part A: Handling Data from Many Participants at Once
### Topic: Group-Level Datasets and Downloading Data Reliably

This section explores what changes when your analysis needs to handle data from an entire group of research participants rather than just one person at a time.

### 🧭 Activity A.1 — Building a Group Dataset

> *Copy the prompt below into your preferred AI tool, then paste the generated code into the code cell beneath it.*
>
> "Act as a neuroscience data analyst helping a researcher scale up from a single participant to a full study. Write a Python script using NumPy that simulates loading and combining data from 50 research participants. The script should:
> 1. For each of 50 participants, generate a data array representing 64 recording channels measured across 1000 time points in 3 experimental conditions.
> 2. Combine all 50 individual participant arrays into a single group-level dataset efficiently, without creating unnecessary copies of the data.
> 3. Report the size and shape of the combined dataset and calculate how much working memory it uses — then estimate how large the dataset would become if the study included 500 participants instead.
> Add plain-language comments explaining what each step does and what the numbers represent."
# 💻 Activity A.1 — Paste your AI-generated Group Dataset code here:
### 🧭 Activity A.2 — Downloading Data Reliably

> *Copy the prompt below into your preferred AI tool, then paste the generated code into the code cell beneath it.*
>
> "Act as a research workflow instructor. Internet connections sometimes drop or get temporarily blocked when downloading large research datasets. Write a Python script that simulates a reliable data download system. The script should:
> 1. Simulate a download function that requests 10 chunks of data from a research repository, one at a time.
> 2. Randomly cause some of the download attempts to fail, to simulate real network interruptions.
> 3. Automatically retry failed downloads, waiting a little longer between each attempt (e.g., wait 1 second after the first failure, 2 seconds after the second, 4 seconds after the third) rather than giving up immediately.
> 4. Print a clear log showing which downloads succeeded, which failed, and how many retries were needed.
> Use plain-language comments explaining why this retry approach is better than simply stopping when an error occurs."
# 💻 Activity A.2 — Paste your AI-generated Reliable Download code here:
### ✍️ Part A Reflection
*Double-click this cell to write your response.*

* **What I observed:** Looking at the dataset sizes from Activity A.1, how does memory usage change as the number of participants grows? What practical limits does this create for a research study?
* **Connecting to key concepts:** Activities A.1 and A.2 demonstrate **Concepts 11, 14, 16, and 43** from your Reference Guide. Describe why a reliable retry system for downloads matters for reproducibility in large studies.

---

## 💻 Part B: Making Analyses Run Faster
### Topic: Running Multiple Analyses at the Same Time and Choosing Efficient Data Formats

This section explores two practical strategies for making research workflows faster when working with large datasets.

### 🧭 Activity B.1 — Running Analyses One-at-a-Time vs. All at Once

> *Copy the prompt below into your preferred AI tool, then paste the generated code into the code cell beneath it.*
>
> "Act as a computing performance instructor. Write a Python script that demonstrates the difference between running a data analysis one participant at a time versus running many participants simultaneously using multiple processor cores. The script should:
> 1. Define a data analysis function that performs a moderately demanding calculation — such as computing a rolling average across a large array.
> 2. Apply this function to 10 separate datasets one at a time, measuring how long the whole process takes.
> 3. Apply the same function to the same 10 datasets simultaneously using Python's multiprocessing library, distributing the work across available processor cores, and measuring how long that takes.
> 4. Display a bar chart comparing the two approaches and calculate the speedup factor.
> Use plain-language comments explaining what is happening and why one approach is faster."
# 💻 Activity B.1 — Paste your AI-generated Simultaneous Processing code here:
### 🧭 Activity B.2 — Saving Data in Efficient Formats

> *Copy the prompt below into your preferred AI tool, then paste the generated code into the code cell beneath it.*
>
> "Act as a data management instructor. Write a Python script that demonstrates the difference between saving research data as a plain text file versus a more efficient binary format. The script should:
> 1. Generate a simulated dataset representing measurements from 100,000 time points across multiple recording channels.
> 2. Save this dataset in two formats: a plain text CSV file (like you would open in a spreadsheet) and an optimized binary file (such as NumPy's .npy format or HDF5).
> 3. Compare the file sizes on disk for both formats.
> 4. Measure and compare how long it takes to load each file back into memory for analysis.
> Use plain-language comments explaining the trade-offs between the two formats and when you would choose each one."
# 💻 Activity B.2 — Paste your AI-generated Data Format Comparison code here:
### ✍️ Part B Reflection
*Double-click this cell to write your response.*

* **What I observed:** From Activity B.1, how much faster was simultaneous processing compared to one-at-a-time? From Activity B.2, how much larger was the plain text file compared to the efficient format?
* **Connecting to key concepts:** Activities B.1 and B.2 demonstrate **Concepts 27, 28, 42, and 43** from your Reference Guide. Explain in plain language when it makes sense to use simultaneous processing and when the overhead might not be worth it.

---

## 📑 What Comes Next

Notebook 3 introduces signal processing — how to clean raw recordings, remove noise, and extract meaningful patterns from brain and behavioral data.

---

## 📖 Reference Guide: 50 Key Concepts for Neuroscience Workflows

Keep this reference guide handy throughout all five pre-workshop notebooks and during the onsite labs. These concepts form the foundation of the workshop's hands-on activities.

### 🧠 Neuroscience & Research Applications (Concepts 1–25)
1. **Brain-Machine Interface (BMI):** A system that connects the brain directly to an external device — bypassing damaged nerves or muscles — so that brain signals can control a robotic limb, cursor, or other tool.
2. **Non-Invasive (EEG) vs. Invasive (Intracortical) Sensors:** Scalp electrodes (EEG) are easy to use but pick up blurry, averaged signals through the skull. Implanted microelectrode arrays record from individual neurons with much greater precision, but require surgery.
3. **Signal Delay (Latency):** The time gap between a brain signal being recorded and a device responding to it. Delays longer than about 50–100 milliseconds feel unnatural to the user of a prosthetic device.
4. **Decoder:** A mathematical or statistical model that translates continuous brain signal patterns into a useful output — such as movement direction, cursor position, or speech intent.
5. **fMRI:** Functional Magnetic Resonance Imaging — a brain scanning method that measures blood oxygen levels as a stand-in for neural activity. When neurons become active, they consume more oxygen, causing a detectable change in the local blood signal.
6. **Voxel:** A small 3D cube of brain tissue in an fMRI image — the brain-imaging equivalent of a pixel. Each voxel contains millions of neurons.
7. **Head Movement Correction:** A processing step that aligns brain scan images across time, compensating for small movements the participant made during the recording session.
8. **Open-Loop vs. Closed-Loop Systems:** An open-loop device follows a fixed program regardless of what the user's brain is doing. A closed-loop device continuously reads incoming signals and adjusts its output in real time based on what it detects.
9. **Deep Brain Stimulation (DBS):** A treatment for conditions like Parkinson's disease in which a small implanted device delivers electrical pulses to specific brain regions to reduce tremor and improve movement.
10. **EMG (Electromyogram):** A recording of the electrical signals produced by muscles when they contract. Often used alongside brain recordings to verify whether a behavioral response actually occurred.
11. **Continuous Recordings vs. Event Markers:** A continuous recording captures an uninterrupted time series of measurements. Event markers are specific timestamps that label when something important happened — such as when a stimulus appeared or a button was pressed.
12. **Signal Drift:** The gradual change in a recorded signal over time, not due to the brain, but due to electrode movement, tissue changes, or electronic drift. Workflows need to account for this to keep analysis accurate over long sessions.
13. **Open Data Repositories:** Publicly accessible online archives (such as DANDI, OpenNeuro, or the Human Connectome Project) where researchers share their raw data so others can analyze or replicate their findings.
14. **Automated Data Download (API):** A method of downloading data directly inside a script using a standardized web link, rather than clicking through a website manually. This makes data access reproducible and audit-able.
15. **Artifact Removal:** The process of identifying and removing unwanted signals — such as electrical noise from the building, muscle movements, or eye blinks — from a raw brain recording before analysis.
16. **Downsampling:** Reducing the number of data points per second in a recording, to save memory and processing time, when the extra detail is not needed for the analysis.
17. **Standard Data Formats (BIDS):** A community-agreed system for naming and organizing brain imaging files so that any researcher or software tool can understand the structure without needing special instructions.
18. **Spectrogram:** A visual display showing how the frequency content of a signal changes over time — useful for seeing when the brain shifts between different rhythmic states such as sleep stages or attention levels.
19. **Nyquist Rule:** A fundamental rule of digital recording: to accurately capture a signal, you must record at least twice as fast as the highest frequency in that signal. Recording too slowly creates false patterns called aliasing.
20. **Local Field Potential (LFP):** An electrical recording that reflects the combined activity of a small cluster of nearby neurons — capturing the general activity level of a local brain region rather than individual cells.
21. **Signal Transfer Function:** A mathematical description of how an input signal is transformed into an output signal by a processing step — useful for predicting what a filter or decoder will do to any given input.
22. **Spike Sorting:** The process of separating a mixed electrical recording from multiple nearby neurons into individual neuron signals, based on the distinct shape of each neuron's electrical discharge.
23. **Machine Learning for Neural Decoding:** Using statistical learning algorithms to automatically find patterns in brain signal data that predict behavior, movement intent, or cognitive state.
24. **Sensory Feedback:** Sending information back to the user of a brain-machine interface — for example, delivering a gentle electrical sensation to the skin to simulate the feeling of touching an object with a prosthetic hand.
25. **Neural Plasticity:** The brain's ability to reorganize its connections over time. Relevant to BMI research because users can learn to control devices more accurately with practice as their brain adapts.

### 💻 Computing & Workflow Fundamentals (Concepts 26–50)
26. **Working Memory (RAM) vs. Permanent Storage:** RAM (working memory) holds data only while the computer is on — it is extremely fast but temporary. The hard drive stores files permanently but is much slower to access.
27. **Processor Core:** A single computing unit inside a central processor (CPU). Most modern computers have multiple cores, allowing several tasks to run at the same time.
28. **CPU vs. GPU:** A CPU handles complex, varied tasks one at a time across a few powerful cores. A GPU handles simple, repetitive tasks across thousands of smaller cores simultaneously — useful for image processing and machine learning.
29. **Memory Overflow:** What happens when a script tries to load more data into working memory (RAM) than the computer has available — causing the program to crash.
30. **Motherboard:** The main circuit board inside a computer that connects all the components — processor, memory, storage, and network — so they can communicate with each other.
31. **Processor Slowdown (Thermal Throttling):** When a processor gets too hot, it automatically slows itself down to prevent damage. This can cause unexpected slowdowns during long analysis runs.
32. **High-Speed Processor Cache:** A small, extremely fast memory area built directly into the processor, used to store frequently needed values so they do not have to be fetched from RAM repeatedly.
33. **Local vs. Cloud Computing:** Running your analysis on the computer in front of you (local) versus running it on a remote server accessed over the internet (cloud). Cloud computing allows access to much more memory and processing power.
34. **Temporary Cloud Workspace:** Cloud computing environments like Google Colab provide a temporary workspace that is automatically cleared when you close the session. Any files you need to keep must be saved to permanent storage before the session ends.
35. **Internet Speed as a Bottleneck:** When downloading large research datasets, the speed of your internet connection often limits how fast data can arrive — regardless of how fast your computer itself is.
36. **Organizing Code into Stages:** Separating a workflow into clearly defined, independent stages — such as one stage for loading data, one for analysis, and one for visualization — makes it much easier to find and fix problems.
37. **Whole Numbers vs. Decimal Numbers in Computing:** Computers store whole numbers (integers) very efficiently. Decimal numbers (floating-point) require more memory and processing time. Choosing the right type for your data can affect both speed and accuracy.
38. **Automated Data Access (API):** A standardized connection that allows one piece of software to request data or services from another automatically — for example, a script that downloads data from a research repository without any manual steps.
39. **Settings Files (JSON/YAML):** Lightweight text files used to store configuration settings, metadata, and parameters for a workflow — making it easy to share, reproduce, or adjust an analysis without changing the code itself.
40. **Processing Delay:** The time between when data arrives in your workflow and when your analysis produces a result. In real-time recording systems, keeping this delay short is critical.
41. **Keeping Stages Independent:** Designing a workflow so that the data analysis stage does not depend on the visualization stage, and vice versa. This means you can update or replace one stage without breaking the others.
42. **Text Files vs. Optimized Data Files:** Saving data as plain text (such as CSV) is easy to read in a spreadsheet but very slow for large datasets. Optimized formats (such as HDF5 or NumPy binary files) are much faster to load and take up less disk space.
43. **Simultaneous Processing (Parallel Computing):** Splitting a large task — such as analyzing 50 participants — into smaller chunks that run at the same time across multiple processor cores, rather than one after another.
44. **Hidden Configuration Settings:** Values that a workflow needs — such as access keys for a data repository — that are stored securely in the operating system rather than written directly into the code, to prevent accidental exposure.
45. **Software Libraries (Dependencies):** Pre-built collections of code (such as NumPy, SciPy, or scikit-learn) that provide ready-made tools for common tasks — so you do not have to write mathematical functions from scratch.
46. **Code Version Tracking (Git):** A system that records every change made to a set of code files over time, along with who made the change and when. This allows teams to collaborate and to restore earlier versions if something goes wrong.
47. **Error Handling:** Code that anticipates things going wrong — such as a missing file or a calculation that produces an undefined result — and responds gracefully rather than crashing the entire workflow.
48. **Data Array:** A structured list of numbers organized so that a computer can perform calculations on all of them efficiently — the basic building block of scientific data analysis.
49. **Data Backlog:** What happens when data arrives faster than your workflow can process it — causing a growing queue that eventually uses up available memory.
50. **Protecting Original Data:** A core rule of reproducible research: never modify your raw data files. Always write processed results to a new, separate file so the original record remains intact.

---

## ✅ Self-Check: What Did You Learn?

*Fill in the table below after completing both activities.*

| Concept Area | Concept Number | Where You Demonstrated It |
|---|---|---|
| Neuroscience | Concept 11 — Continuous recordings vs. event markers | [ Enter Cell ID ] |
| Neuroscience | Concept 14 — Automated data download | [ Enter Cell ID ] |
| Neuroscience | Concept 16 — Downsampling | [ Enter Cell ID ] |
| Computing | Concept 27 — Processor cores | [ Enter Cell ID ] |
| Computing | Concept 28 — CPU vs. GPU | [ Enter Cell ID ] |
| Computing | Concept 43 — Simultaneous processing | [ Enter Cell ID ] |
