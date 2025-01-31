document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById('table-body');
    const numRows = 997;

    for (let i = 1; i <= numRows; i++){
        const row = document.createElement('div');
        row.classList.add('row');

        row.innerHTML = `
            <div>${i}</div>
            <div>Name ${i}</div>
            <div>LastName ${i}</div>
            <div>Name${i}@test.com.br</div>
            <div>
                <button>Action</button>
            </div>
        `;

        tableBody.appendChild(row);
    }
});