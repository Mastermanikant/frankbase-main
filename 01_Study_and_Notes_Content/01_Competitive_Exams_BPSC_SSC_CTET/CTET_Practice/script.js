document.addEventListener('DOMContentLoaded', () => {
    const questionEl = document.getElementById('question');
    const optionsEl = document.getElementById('options');
    const nextBtn = document.getElementById('next-btn');
    const showAnswerBtn = document.getElementById('show-answer-btn');
    const questionBox = document.getElementById('question-box');
    const resultBox = document.getElementById('result-box');
    const loadingEl = document.getElementById('loading');
    const currentQEl = document.getElementById('current-question');
    const totalQEl = document.getElementById('total-questions');
    const scoreEl = document.getElementById('score');
    const explanationBox = document.getElementById('explanation');
    const explanationText = document.getElementById('explanation-text');

    let questions = [];
    let currentQuestionIndex = 0;
    let score = 0;

    // Load questions from JSON
    fetch('questions.json')
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            return response.json();
        })
        .then(data => {
            questions = data;
            totalQEl.textContent = questions.length;
            loadingEl.classList.add('hidden');
            if (questions.length > 0) {
                questionBox.classList.remove('hidden');
                loadQuestion();
            } else {
                questionBox.innerHTML = '<p>कोई प्रश्न उपलब्ध नहीं हैं। कृपया questions.json चेक करें।</p>';
                questionBox.classList.remove('hidden');
            }
        })
        .catch(error => {
            loadingEl.textContent = 'प्रश्न लोड करने में त्रुटि। कृपया सुनिश्चित करें कि questions.json फाइल मौजूद है।';
            console.error('Error loading questions:', error);
        });

    function loadQuestion() {
        resetState();
        const currentQuestion = questions[currentQuestionIndex];
        currentQEl.textContent = currentQuestionIndex + 1;
        questionEl.innerHTML = currentQuestion.question; // Using innerHTML to support possible formatting

        currentQuestion.options.forEach((option, index) => {
            const button = document.createElement('button');
            button.innerText = option;
            button.classList.add('option-btn');
            button.dataset.index = index;
            button.addEventListener('click', selectAnswer);
            optionsEl.appendChild(button);
        });
    }

    function resetState() {
        nextBtn.style.display = 'none';
        showAnswerBtn.style.display = 'block';
        explanationBox.classList.add('hidden');
        while (optionsEl.firstChild) {
            optionsEl.removeChild(optionsEl.firstChild);
        }
    }

    function selectAnswer(e) {
        const selectedBtn = e.target;
        const currentQuestion = questions[currentQuestionIndex];
        const correctIndex = currentQuestion.answer; // Assuming 0-based index or string match

        // Disable all buttons
        Array.from(optionsEl.children).forEach(button => {
            button.disabled = true;
            if (parseInt(button.dataset.index) === correctIndex) {
                button.classList.add('correct');
            }
        });

        if (parseInt(selectedBtn.dataset.index) === correctIndex) {
            selectedBtn.classList.add('correct');
            score++;
            scoreEl.textContent = score;
        } else {
            selectedBtn.classList.add('wrong');
        }

        if (currentQuestion.explanation) {
            explanationText.textContent = currentQuestion.explanation;
            explanationBox.classList.remove('hidden');
        }

        showAnswerBtn.style.display = 'none';
        nextBtn.style.display = 'block';
    }

    showAnswerBtn.addEventListener('click', () => {
        const currentQuestion = questions[currentQuestionIndex];
        const correctIndex = currentQuestion.answer;
        
        Array.from(optionsEl.children).forEach(button => {
            button.disabled = true;
            if (parseInt(button.dataset.index) === correctIndex) {
                button.classList.add('correct');
            }
        });

        if (currentQuestion.explanation) {
            explanationText.textContent = currentQuestion.explanation;
            explanationBox.classList.remove('hidden');
        }
        
        showAnswerBtn.style.display = 'none';
        nextBtn.style.display = 'block';
    });

    nextBtn.addEventListener('click', () => {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            loadQuestion();
        } else {
            showScore();
        }
    });

    function showScore() {
        questionBox.classList.add('hidden');
        resultBox.classList.remove('hidden');
        document.getElementById('final-score').textContent = `${score} / ${questions.length}`;
    }
});
