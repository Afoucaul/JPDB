package words;
import genericData.*;
import kanjis.Kanji;
import kanjis.Character;
import exceptions.*;
import java.util.*;

public class Word extends DataElement {
	private String reading;
	private int studiedTimes;
	private List<PositionInWord> writing;
	
	public Word(List<PositionInWord> writing, String reading, List<String> meanings) {
		super(meanings);
		this.studiedTimes = 0;
		this.writing = new ArrayList();
		for(PositionInWord position : writing) {
			this.writing.add(position);
		}
	}
	
	public Word(List<PositionInWord> writing, String reading, List<String> meanings, int studiedTimes) {
		this(writing, reading, meanings);
		this.studiedTimes = studiedTimes;
	}

	public void study() {
		this.studiedTimes++;
	}
	
	public boolean isRelatedTo(Kanji kanji) {
		boolean flag = false;
		for(PositionInWord position : this.writing) {
			flag = position.getCharacter().getChar() == kanji.getCharacter();
			if(flag)
				return true;
		}
		return false;
	}
	
	public Character getCharacter(int position) throws NotInWordException {
		for(PositionInWord character : writing) {
			if(character.getPosition() == position) {
				return character.getCharacter();
			}
		}
		throw new NotInWordException("Bad position given");
	}
	
	public boolean isWritten(String writing) {
		try {
			for(int i=0; i<writing.length(); i++) {
				if(this.getCharacter(i+1).getChar() != writing.substring(i, i+1)) {
					return false;
				}
			}
			return true;
		}
		catch(NotInWordException e) {
			return false;
		}
	}
}
