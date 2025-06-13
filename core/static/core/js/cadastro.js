function alternarFormulario() {
  const tipo = document.querySelector(
    'input[name="tipo_usuario"]:checked',
  ).value;
  const pessoaFields = document.getElementById('pessoa-fields');
  const ongFields = document.getElementById('ong-fields');

  if (tipo === 'PESSOA') {
    pessoaFields.style.display = 'block';
    ongFields.style.display = 'none';

    document.getElementById('cpf').required = true;
    document.getElementById('nome_ong').required = false;
    document.getElementById('cnpj').required = false;
    document.getElementById('responsavel').required = false;
  } else {
    pessoaFields.style.display = 'none';
    ongFields.style.display = 'block';

    document.getElementById('cpf').required = false;
    document.getElementById('nome_ong').required = true;
    document.getElementById('cnpj').required = true;
    document.getElementById('responsavel').required = true;
  }
}
