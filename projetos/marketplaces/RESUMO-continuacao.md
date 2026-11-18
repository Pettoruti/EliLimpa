# Resumo para continuar: Bling × Amazon, Magalu, TikTok Shop, kits e cadastros

Situação em 18/11/2026. Cole este resumo no início da nova conversa.

## Onde está tudo
- **Caderno (checklist visual com bolinhas):** https://claude.ai/artifact/4V5JjgahCS351jNd4kLQYG. Os dados ficam na coleção `tarefas`, com status aberto, andamento, aguardando, bloqueado ou feito. As frentes são Base Bling, Amazon, Magalu, TikTok Shop e Site Nuvemshop. São 4 etapas: até 13/11, 20/11, 27/11 (Black Friday) e 11/12.
- **Repositório:** `pettoruti/elilimpa`, branch `claude/bling-marketplace-integration-969z8r`
  - `projetos/marketplaces/checklist-integracao.html`: a página do caderno
  - `projetos/precos/precos_sugeridos_63_produtos.xlsx`: os preços aprovados por canal
  - `produtos/gel-leve-brisa/fotos/`: as fotos tratadas do gel, `montar.py` e `prompts_fotos_em_uso.md`

## Regras combinadas
- **Margem:** alvo de 15% e mínima de 6%. Simples Nacional de 4%. Preços terminam em ,90.
- **Taxas usadas:**
  - Nuvemshop: 4,69% + R$ 0,35.
  - ML Clássico: 14%, mais custo fixo de R$ 5,65 (até R$ 19), R$ 6,85 (R$ 19–48,99) ou R$ 8,15 (R$ 49–78,99). A partir de R$ 79, o frete grátis é por conta do vendedor.
  - ML Premium: 19%.
  - Shopee: 20% + R$ 4.
- **Preço base no Bling:** é o do ML Clássico nos produtos vendidos em todos os canais. Nos produtos "só Nuvemshop", é o da Nuvemshop. Os preços da Nuvemshop e da Shopee vão na aba **Lojas (Multiloja)** de cada produto. A ferramenta do Bling que o Claude usa não grava esses preços, então isso é manual.
- **"Cores Sortidas":** é o nome padrão quando a cor pode variar.
- **Vassouras compradas sem cabo:** são vendidas com cabo Caiçara de 1,20m (R$ 3,66). O preço de compra é o da vassoura e o preço de custo é vassoura + cabo.
- **Produtos de outras marcas:** vão como "Kit" com isenção de código de barras, ou como genérico.
- **Antes de mexer em preço, publicar, excluir ou entrar em promoção:** pedir o ok do Raul.

## Feito no Bling (até 18/11)
- **Custos:** gravados com a Lotus como fornecedor em cerca de 140 produtos, a partir de 9 notas da Lotus. Itens em pacote foram convertidos para a unidade em que o Bling vende (fardo ÷ 16, pacote ÷ 6 etc.).
- **Produtos novos:** 63 cadastrados, com descrição completa (texto de venda, ficha técnica, modo de uso, cuidados) e preço aprovado.
- **Pedidos de compra:** os nº 3, 11 e 12 estão ativos, das notas que não estavam importadas. Os nº 2 e 4 a 10 foram cancelados, porque eram notas já importadas (são 111 notas de entrada no Bling). Nenhum estoque foi lançado. Não há conta a pagar, porque as notas foram pagas à vista.
- **Kits do site, com composição e estoque virtual:**

| Código | Kit | Preço | Custo dos produtos |
|---|---|---|---|
| ELI-KIT-BANHEIRO | Banheiro Brilhando | R$ 49,90 | R$ 26,08 |
| ELI-KIT-COZINHA | Cozinha Sem Gordura | R$ 46,90 | R$ 28,06 |
| ELI-KIT-FAXINA | Faxina na Casa Toda | R$ 89,90 | R$ 47,41 |
| ELI-KIT-REPOSICAO | Reposição do Mês | R$ 89,90 | R$ 47,30 |

  A embalagem é feita com caixas reaproveitadas, então o custo dela é zero. O frete grátis vale só para Faxina e Reposição, só em SP e região, e se configura na Nuvemshop.
- **Gel Leve Brisa Lavanda:**
  - Refil (código 1651): custo R$ 8,17, preço R$ 13,90, só na Nuvemshop, código de barras 7898178361398.
  - Com aplicador (código 13835): custo R$ 8,61, código de barras 7898178361367. Vendido sozinho no ML dá prejuízo, então só vai para a Nuvemshop.
  - Kit ELI-KIT-LEVEBRISA-1A2R (1 aplicador + 2 refis): custo R$ 24,95. Preço base R$ 47,90, Nuvemshop R$ 39,90, ML Premium R$ 53,90.

## Pendências
1. **Web Sellers (Amazon):** fechado o pacote de 10 produtos por R$ 700.
   - SKU na Amazon = código do Bling. Fotos e Brand Registry ficam de fora.
   - Falta:
     - mandar os dados para o contrato (razão social RAUL EDUARDO PETTORUTI 21255719869, CNPJ 26.663.733/0001-08, responsável Raul Eduardo Pettoruti, forma de pagamento);
     - ler o contrato;
     - conferir o nome do recebedor do Pix (CNPJ 37.604.498/0001-01);
     - enviar a lista e as fotos.
   - Os 10 produtos e seus códigos no Bling:

| Produto | Código no Bling |
|---|---|
| Enzmax 500g | 7898925601000 |
| Pano Perfect Pro 50x60 | 972258 |
| Kit Leve Brisa | ELI-KIT-LEVEBRISA-1A2R |
| Sabonete Premisse Lavanda 5L | 1100885 |
| Saco Leal 50L rolo | LEAL050ROLOPT |
| Luva Nitrílica Bompack G | 1612 |
| Papel Toalha Toppel 22x21 | 16286 |
| Copo 180ml PP Ultra | 14494 |
| Fibra Bettanin Slim C10 | 12637 |
| Limpa Porcelanato Azulim 5L | 16898 |

   - Lista de 20 de reserva: Kit Reposição, Mop Perfect, Kit 2 Premisse, Lixeira 30L JSN, Kit Toucas Bompack, Cai-Cai Baby, Saco Leal 100L BL8, Pá JSN, Plush 2 em 1 5L, Filme PVC Tecfilm.
2. **Multiloja:** pôr os preços da Nuvemshop e da Shopee dos 35 produtos "todos os canais" (estão na planilha) e os do kit Leve Brisa.
3. **Vassoura Nylon N4 (código 18436):** no fornecedor, preço de compra 8,85 e custo 12,51. O Raul editou, mas não estava gravado em 16/11. Conferir. Fazer o mesmo nas vassouras Brubalar, Ceci, Piaçava N4 e Gari 15002.
4. **Brilha Inox Azulim (NF 716014):** a nota cobra R$ 35,38 a unidade. Confirmar se chegaram 2 frascos ou 2 caixas.
5. **Repensar a compra:** Tira Limo Veja X-14 e Repelente Raid (caixa com 12) têm custo acima do preço de varejo.
6. **Kits:** falta peso, medidas e fotos dos 4 kits do site e do kit Leve Brisa. Fotos em uso do gel: usar os prompts no Gemini.
7. **Kit de panos com 6:** ideia do Raul. A Lotus já vende o pano de chão xadrez e o saco alvejado em pacote com 6.
8. **Site Nuvemshop:** criar a categoria "Kits de Limpeza" no menu e a vitrine "Kits prontos" na página inicial.
9. **Amazon, Magalu e TikTok Shop:** as contas, documentos e integração no Bling seguem a lista do caderno (etapas 1 a 4).
10. **Marca vazia:** Guardanapo Baby 14x14 e Rodo Aplicador de Cera.
