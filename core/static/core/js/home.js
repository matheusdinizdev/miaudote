document.getElementById('btn-limpar').addEventListener('click', function () {
  const form = document.getElementById('form-filtros');
  form.tipo.value = '';
  form.porte.value = '';
  form.idade_min.value = '';
  form.idade_max.value = '';
  form.submit();
});
