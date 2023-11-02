package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink{

    private String name;

    public DrinkImpl() {
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public boolean isFizzy() {
        return this.name != null && this.name.equalsIgnoreCase("ScottCola");
    }
}
