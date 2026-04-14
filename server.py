from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/data")
def summary():
    d = {
        'citations': [
          {
            'title': "Repression of Connexin26 hemichannel activity protects the barrier function of respiratory airway epithelial cells against LPS-induced alteration.",
            'journal': "In Cell Communication and Signaling (CCS)",
            'published_date': "16 May 2025",
            'authors': "Lehrich, T., Dierks, A., et al.",
            'image_urls': [
              "https://images.citeab.com/s--yIgHlsc2--/t_full_trimmed/v1589975864/in0ys1ewznpjm5eaqg1k.jpg",
              "https://images.citeab.com/s--lsr0HhTx--/t_full_trimmed/v1559132179/fnss1culw4hwfpo3gucu.jpg",
              "https://images.citeab.com/s--nRAg40TM--/t_full_trimmed/v1559132181/s1n6i5d2mzsygko72mrw.jpg"
            ]
          },
          {
            'title': "CRISPR-Cas9 mediated gene editing in human stem cells: Advances and challenges.",
            'journal': "Nature Biotechnology",
            'published_date': "10 March 2024",
            'authors': "Smith, J., Patel, R., Lee, H.",
            'image_urls': [
                "https://images.citeab.com/s--CPpphony--/t_full_trimmed/v1589975831/ahjbvgpnxznxfkcexyxk.jpg",
                "https://images.citeab.com/s--Jvrq8N2L--/t_full_trimmed/v1589975832/ymbuwdrvgp6fklpy39om.jpg",
                "https://images.citeab.com/s--g-v-ZPrx--/t_full_trimmed/v1589975859/geyvkxfo3enzh0v6rtp2.jpg",
                "https://images.citeab.com/s--85BBD7UI--/t_full_trimmed/v1589975859/fblpruvs0fcn0buvvaoo.jpg",
                "https://images.citeab.com/s--lZ9ptu3O--/t_full_trimmed/v1589975866/upthov2hcuqwxxrreorn.jpg"
            ]
          },
          {
            'title': "Machine learning approaches for cancer prognosis prediction.",
            'journal': "Bioinformatics",
            'published_date': "22 January 2023",
            'authors': "Chen, L., Kumar, S., Wang, Y.",
            'image_urls': [
              "https://images.citeab.com/s--UNpOYYAH--/t_full_trimmed/v1589975826/l0c86ijfxwvuo6yullho.jpg",
              "https://images.citeab.com/s--efcKdfnm--/t_full_trimmed/v1589975828/nlvbspfxeyxt3lx4t0zj.jpg"
            ]
          },
          {
            'title': "The role of gut microbiota in metabolic diseases.",
            'journal': "Trends in Endocrinology & Metabolism",
            'published_date': "5 July 2022",
            'authors': "Garcia, M., O'Neill, P., Singh, T.",
            'image_urls': []
          },
          {
            'title': "Quantum computing: Current status and future prospects.",
            'journal': "Science Advances",
            'published_date': "18 November 2025",
            'authors': "Nguyen, D., Fischer, B., Zhao, Q.",
            'image_urls': [
              "https://images.citeab.com/s--AdTa3uki--/t_full_trimmed/v1589975803/d0s2j1nmxs3c9h6vqfe3.jpg",
              "https://images.citeab.com/s--IBi6TcSz--/t_full_trimmed/v1587995967/lcfujqslot7hdqp5nbwn.jpg",
              "https://images.citeab.com/s--_P9pbpGF--/t_full_trimmed/v1638533480/yefiguebtor35h49s2qd.jpg",
              "https://images.citeab.com/s--8wXI3Zyq--/t_full_trimmed/v1589975805/h0u1nu2kps66ycjvk3rx.jpg",
              "https://images.citeab.com/s--4v9MXUa4--/t_full_trimmed/v1587995962/s8rxuucgkqrylhydswmv.jpg",
              "https://images.citeab.com/s--l4-Oi4kv--/t_full_trimmed/v1587995968/qdypry86makumm9v5ijw.jpg",
              "https://images.citeab.com/s--oMGiiB2w--/t_full_trimmed/v1589975811/xqv9dqj9ncqd9ha5oljt.jpg",
              "https://images.citeab.com/s--W5NuL4aT--/t_full_trimmed/v1587995975/n01udrmvsjzgag5qhntb.jpg",
              "https://images.citeab.com/s--nl32rZqR--/t_full_trimmed/v1587995984/luws2bhl7rhzd2jfrvpy.jpg",
              "https://images.citeab.com/s--Mb17lqBv--/t_full_trimmed/v1587995998/hwki4jgfpzpjj61i9ifr.jpg"
            ]
          },
          {
            'title': "Deep learning for image-based plant disease detection.",
            'journal': "Computers and Electronics in Agriculture",
            'published_date': "30 September 2023",
            'authors': "Ali, S., Brown, K., Evans, J.",
            'image_urls': []
          },
          {
            'title': "Renewable energy integration in smart grids: A review.",
            'journal': "Renewable and Sustainable Energy Reviews",
            'published_date': "12 February 2024",
            'authors': "Martinez, F., Rossi, L., Kim, S.",
            'image_urls': []
          },
          {
            'title': "Advances in nanomaterials for drug delivery systems.",
            'journal': "'Journal' of Controlled Release",
            'published_date': "8 August 2025",
            'authors': "Zhang, X., Mehta, P., Silva, R.",
            'image_urls': []
          },
          {
            'title': "Climate change impacts on global biodiversity.",
            'journal': "Global Change Biology",
            'published_date': "2 April 2022",
            'authors': "Johnson, E., Müller, T., Ahmed, L.",
            'image_urls': []
          },
          {
            'title': "Wearable biosensors for real-time health monitoring.",
            'journal': "Sensors and Actuators B: Chemical",
            'published_date': "15 December 2023",
            'authors': "Kumar, V., Lee, S., Thompson, G.",
            'image_urls': []
          }
        ],
        'allImageUrls': [
          "https://images.citeab.com/s--hDtYlWxD--/t_full_trimmed/v1589975412/k18gqxihiyatelq3iguj.jpg",
          "https://images.citeab.com/s--SHOIZu5Z--/t_full_trimmed/v1589975451/linrxgmmpjsr46elzdla.jpg",
          "https://images.citeab.com/s--rxJOESbC--/t_full_trimmed/v1589975451/swlztwvt8zbxaxugwei1.jpg",
          "https://images.citeab.com/s--WftJeDz7--/t_full_trimmed/v1589975449/cuzfk8jdrxyvsqzpqbl2.jpg",
          "https://images.citeab.com/s--cijPDwaV--/t_full_trimmed/v1587995669/bp3yb5eqjcuuug34lxiq.jpg",
          "https://images.citeab.com/s--8oHMIS_l--/t_full_trimmed/v1590582695/gnnjxvoqxohiabvhidrl.jpg",
          "https://images.citeab.com/s--0mMyDOBJ--/t_full_trimmed/v1589977570/gqfwlqwagzzu7y27icwf.jpg",
          "https://images.citeab.com/s--2fv-q4Uo--/t_full_trimmed/v1589975451/zl4z4lwufm9b6r7nb32x.jpg"
        ]
    }
    print(request.args.get('pubmed') == 'true')
    if request.args.get('pubmed') == 'true':
        d['citations'] = d['citations'][:2]
    response = jsonify(d)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response