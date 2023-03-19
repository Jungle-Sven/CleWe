type Skill = {
  id: number;
  topic: string;
  title: string;
  experience: number;
  level: number;
};

export type Trophy = {
  id: number;
  tx_hash?: string; // depending on this field system assumes wether a trophy is collected/minted or not
  img_url: string;
  description: string;
};

export type UserDTO = {
  id: number;
  nickname: string;
  level: number;
  level_total_exp: number;
  exp_to_next_level: number;
  skills: Skill[];
  completed_quests: QuestDTO[];
  trophies: Trophy[];
};

export type QuestDTO = {
  id: number;
  name: string;
  slug: string;
  topic: string;
  skill_reward: number;
  description: string;
  difficulty: number;
  exp_reward: number;
};
