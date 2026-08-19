const fileInput = document.getElementById("pdf-file");
const fileName = document.getElementById("file-name");
const uploadBtn = document.getElementById("upload-btn");
const uploadStatus = document.getElementById("upload-status");

const currentDocument = document.getElementById("current-document");

const questionInput = document.getElementById("question-input");
const sendBtn = document.getElementById("send-btn");
const chatMessages = document.getElementById("chat-messages");

let currentDocumentId = null;
// ============================
// FILE SELECT
// ============================

fileInput.addEventListener("change", () => {

    const file = fileInput.files[0];

    if (!file) {
        fileName.textContent = "Chưa chọn file";
        return;
    }

    if (file.type !== "application/pdf") {
        fileName.textContent = "File không hợp lệ";
        fileInput.value = "";
        return;
    }

    fileName.textContent = file.name;
});


// ============================
// UPLOAD PDF
// ============================

uploadBtn.addEventListener("click", async () => {

    const file = fileInput.files[0];

    if (!file) {
        uploadStatus.textContent = "Vui lòng chọn file PDF";
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    uploadBtn.disabled = true;
    uploadStatus.textContent = "Đang upload...";

    try {

        const response = await fetch(
            "/api/upload_pdf",
            {
                method: "POST",
                body: formData,
                credentials: "include"
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Upload thất bại"
            );
        }

        uploadStatus.textContent =
            "Upload thành công";

        currentDocument.textContent =
            data.filename || file.name;

        currentDocumentId = data.document_id;
        addMessage(
            "assistant",
            `File "${data.filename || file.name}" đã được upload thành công!\n\nBạn có thể đặt câu hỏi về tài liệu.`
        );

    } catch (error) {

        console.error(error);

        uploadStatus.textContent =
            error.message;

    } finally {

        uploadBtn.disabled = false;
    }
});


// ============================
// ADD MESSAGE
// ============================

function addMessage(role, content) {

    const message = document.createElement("div");

    message.classList.add(
        "message",
        role
    );

    const avatar = document.createElement("div");

    avatar.classList.add(
        "message-avatar"
    );

    avatar.textContent =
        role === "user" ? "You" : "AI";


    const messageContent =
        document.createElement("div");

    messageContent.classList.add(
        "message-content"
    );

    messageContent.textContent = content;


    message.appendChild(avatar);
    message.appendChild(messageContent);

    chatMessages.appendChild(message);

    chatMessages.scrollTop =
        chatMessages.scrollHeight;
}


// ============================
// SEND QUESTION
// ============================

async function sendQuestion() {

    const question =
        questionInput.value.trim();

    if (!question) {
        return;
    }


    // Show user message
    addMessage(
        "user",
        question
    );

    questionInput.value = "";

    sendBtn.disabled = true;

    try {

        const response = await fetch(
            "/api/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                credentials: "include",

                body: JSON.stringify({
                    // document_id: currentDocumentId,
                    document_id: "TieuDiemThang_1_2026_Truong",
                    question: question
                })
            }
        );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Có lỗi xảy ra"
            );
        }


        // Show AI response
        addMessage(
            "assistant",
            data.answer
        );


    } catch (error) {

        console.error(error);

        addMessage(
            "assistant",
            "Xin lỗi, đã xảy ra lỗi: " +
            error.message
        );

    } finally {

        sendBtn.disabled = false;

        questionInput.focus();
    }
}


// ============================
// SEND BUTTON
// ============================

sendBtn.addEventListener(
    "click",
    sendQuestion
);


// ============================
// ENTER TO SEND
// ============================

questionInput.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendQuestion();
        }
    }
);