export default function Field({ ...props }) {
  return (
    <fieldset>
      <figure>
        <img src={props.albumcover} alt={`capa da música ${props.alt}`} />
      </figure>
      <div>
        <div>
          <span>{props.nameSong}</span>
          <span>{props.nameArtist}</span>
        </div>
        <input type="checkbox" name={props.id} id={props.id} />
      </div>
    </fieldset>
  )
}
