// Atualiza a tabela de produtos com os dados do modal
document.getElementById("btn-add-produto").addEventListener("click", function () {
    const modal = new bootstrap.Modal(document.getElementById("produtoModal"));
    modal.show();
})

// Filtra produtos no modal
document.getElementById("produto-filter").addEventListener("input", function () {
    const termo = this.value.toLowerCase ();
    document.querySelectorAll("#produto-list tr").forEach(tr => {
        const texto = tr.textContent.toLowerCase();
        tr.style.display = texto.includes(termo) ? "" : "none";
    });
});

// Função para adiciona linha de produto à tabela
document.querySelectorAll(".btn-selecionar").forEach(btn => {
    btn.addEventListener("click", function () {
        const id = this.getAttribute("data-id");
        const nome = this.getAttribute("data-nome");
        const preco = parseFloat(this.getAttribute("data-preco"));

        const tbody = document.getElementById("produtos-body");

        const tr = document.createElement("tr");
        tr.innerHTML = `
        <td>
        <input type="hidden" name="produto_id[]" value="${id}">
        ${nome}
        </td>
        <td><input type="number" name="quantidade[]" value="1" min="1" class="form-control quantidade-input"
    oninput="atualizaSubtotal(this)"></td>
        <td>R$ <span class="preco">${preco.toFixed(2)}</span></td>
        <td>R$ <span class="subtotal">0.00</span></td>
        <td>
            <button type="button" class="btn btn-danger btn-sm" onclick="removerLinha(this)">
                <i class="bi bi-trash"></i>
            </button>
            </td>
            `;
            tbody.appendChild(tr);
            atualizaSubtotal(tr.querySelector("input.quantidade-input")); // Atualiza subtotal inicial
            bootstrap.Modal.getInstance(document.getElementById("produtoModal")).hide();
    });
});

//Remove uma linha da tabela
function removerLinha(button) {
    button.closest("tr").remove();
    atualizaTotalGeral();
}

// Atualiza subtotal de um item
function atualizaSubtotal(input) {
    const tr = input.closest("tr");
    const qtd = parseInt(input.value) || 0;
    const preco = parseFloat(tr.querySelector(".preco").textContent.replace(',', '.')) || 0;
    const subtotal = qtd * preco;

    tr.querySelector(".subtotal").textContent = subtotal.toFixed(2);
    atualizaTotalGeral();
}

// Calcula o total geral do pedido
function atualizaTotalGeral() {
    const subtotais = document.querySelectorAll("#produtos-body .subtotal");
    let total = 0;
    subtotais.forEach(span => {
        total += parseFloat(span.textContent.replace(',', '.'));
    });
    document.getElementById("total-geral").textContent = total.toFixed(2);
}