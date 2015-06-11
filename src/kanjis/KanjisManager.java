package kanjis;
import java.util.*;
import exceptions.*;

public class KanjisManager {
	private List<Kanji> kanjis;
	
	public KanjisManager() {
		this.kanjis = new ArrayList();
	}
	
	public void loadKanjis() {
		
	}
	
	public void addToTable(Kanji kanji) {
		
	}
	
	public void removeFromTable(Kanji kanji) {
		
	}
	
	public Kanji searchByCharacter(String character) throws NotInListException {
		for(Kanji kanji : kanjis) {
			if(kanji.getCharacter() == character) {
				return kanji;
			}
		}
		throw new NotInListException("No kanji was found");
	}
	
	public Kanji searchByMeanings(List<String> meanings) throws NotInListException {
		for(Kanji kanji : kanjis) {
			boolean flag = true;
			for(String meaning : meanings) {
				flag &= kanji.means(meaning);
			}
			if(flag)
				return kanji;
		}
		throw new NotInListException("No kanji was found");
	}
}
