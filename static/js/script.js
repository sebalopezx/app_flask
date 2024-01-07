document.addEventListener('DOMContentLoaded', () => {
    const botonesDelete = document.querySelectorAll('.btn-delete');
    if (botonesDelete) {
        const listaBotones = Array.from(botonesDelete);
        listaBotones.forEach((btn) => {
            btn.addEventListener('click', (e) => {
                if (!confirm("¿Desea eliminar el registro?")){
                    e.preventDefault();
                }
            })
        })
    }
})

