package genericData;
import kanjis.Character;

public class PositionInWord {
	private Character character;
	private int position;
	
	public PositionInWord(Character character, int position) {
		this.character = character;
		this.position = position;
	}
	
	public Character getCharacter() {
		return character;
	}
	
	public int getPosition() {
		return position;
	}
}
