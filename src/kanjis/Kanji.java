package kanjis;

import java.util.List;

public class Kanji extends Character {
	private int strokes;
	
	public Kanji(String character, List<String> meanings, int strokes) {
		super(character, meanings);
		this.strokes = strokes;
		
	}
	
	public boolean isEqual(Kanji other) {
		return this.getCharacter() == other.getCharacter();
	}
	
	public String getCharacter() {
		return super.getChar();
	}
	
}
