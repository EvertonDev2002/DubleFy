import spotifyLogo from "../assets/Spotify.svg"

export default function Header({...props}) {
  return (
    <header className={props.className}>
      <nav>
        <span>DublueFy</span>
        <figure>
          <img src={spotifyLogo} alt="Logo do Spotify" />
        </figure>
      </nav>
    </header>
  )
}
