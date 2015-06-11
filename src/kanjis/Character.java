package kanjis;

import genericData.DataElement;
import java.util.List;

public class Character extends DataElement {
	private String character;
	
	public Character() {}
	
	public Character(String character, List<String> meanings) {
		super(meanings);
		this.character = character;
	}
	
	public String getChar() {
		return character;
	}
	
	public boolean isEqual(Character other) {
		return this.character == other.getChar();
	}
}
