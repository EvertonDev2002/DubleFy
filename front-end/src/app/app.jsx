import Header from "../components/header"
import Field from "../components/field"
import albumcover from "../assets/albumcover.jpg"

export default function App() {
  return (
    <div className="main-container">
      <Header className="header" />
      <main className="content">
        <section>
          <p>Suas Músicas</p>
          <form>
            <div>
              <Field
                albumcover={albumcover}
                alt={"Re:Re"}
                nameSong={"Re:Re"}
                nameArtist={"ASIAN KUNG-FU GENERATION "}
              />
            </div>
            <button>Remover</button>
          </form>
        </section>
      </main>
    </div>
  )
}
